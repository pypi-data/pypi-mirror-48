#!/usr/bin/env python
"""A flow to enrol new clients."""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from grr_response_core.lib import queues
from grr_response_core.lib import rdfvalue
from grr_response_core.lib import utils
from grr_response_core.lib.rdfvalues import client as rdf_client
from grr_response_core.lib.rdfvalues import crypto as rdf_crypto
from grr_response_core.lib.rdfvalues import structs as rdf_structs
from grr_response_proto import flows_pb2
from grr_response_server import aff4
from grr_response_server import client_index
from grr_response_server import data_store
from grr_response_server import events
from grr_response_server import flow
from grr_response_server import flow_base
from grr_response_server import message_handlers
from grr_response_server.aff4_objects import aff4_grr
from grr_response_server.databases import db
from grr_response_server.rdfvalues import objects as rdf_objects


class CAEnrolerArgs(rdf_structs.RDFProtoStruct):
  protobuf = flows_pb2.CAEnrolerArgs
  rdf_deps = [
      rdf_crypto.Certificate,
  ]


@flow_base.DualDBFlow
class CAEnrolerMixin(object):
  """Enrol new clients."""

  args_type = CAEnrolerArgs

  def Start(self):
    """Sign the CSR from the client."""
    if self.args.csr.type != rdf_crypto.Certificate.Type.CSR:
      raise ValueError("Must be called with CSR")

    csr = rdf_crypto.CertificateSigningRequest(self.args.csr.pem)
    # Verify the CSR. This is not strictly necessary but doesn't harm either.
    try:
      csr.Verify(csr.GetPublicKey())
    except rdf_crypto.VerificationError:
      raise flow.FlowError("CSR for client %s did not verify: %s" %
                           (self.client_id, csr.AsPEM()))

    # Verify that the CN is of the correct form. The common name should refer
    # to a client URN.
    self.cn = rdf_client.ClientURN.FromPublicKey(csr.GetPublicKey())
    if self.cn != csr.GetCN():
      raise ValueError("CSR CN %s does not match public key %s." %
                       (csr.GetCN(), self.cn))

    logging.info("Will sign CSR for: %s", self.cn)

    cert = rdf_crypto.RDFX509Cert.ClientCertFromCSR(csr)

    # This check is important to ensure that the client id reported in the
    # source of the enrollment request is the same as the one in the
    # certificate. We use the ClientURN to ensure this is also of the correct
    # form for a client name.
    if self.cn != self.client_id:
      raise flow.FlowError("Certificate name %s mismatch for client %s" %
                           (self.cn, self.client_id))

    now = rdfvalue.RDFDatetime.Now()
    if data_store.AFF4Enabled():
      with aff4.FACTORY.Create(
          self.client_id, aff4_grr.VFSGRRClient, mode="rw",
          token=self.token) as client:
        # Set and write the certificate to the client record.
        client.Set(client.Schema.CERT, cert)
        client.Set(client.Schema.FIRST_SEEN, now)

        index = client_index.CreateClientIndex(token=self.token)
        index.AddClient(client)

    if data_store.RelationalDBEnabled():
      data_store.REL_DB.WriteClientMetadata(
          self.client_id, certificate=cert, fleetspeak_enabled=False)
      index = client_index.ClientIndex()
      index.AddClient(rdf_objects.ClientSnapshot(client_id=self.client_id))

    # Publish the client enrollment message.
    events.Events.PublishEvent(
        "ClientEnrollment", self.client_urn, token=self.token)

    self.Log("Enrolled %s successfully", self.client_id)


enrolment_cache = utils.FastStore(5000)


class Enroler(flow.WellKnownFlow):
  """Manage enrolment requests."""

  well_known_session_id = rdfvalue.SessionID(
      queue=queues.ENROLLMENT, flow_name="Enrol")

  def ProcessMessage(self, message):
    """Begins an enrollment flow for this client.

    Args:
        message: The Certificate sent by the client. Note that this message is
          not authenticated.
    """
    cert = rdf_crypto.Certificate(message.payload)

    queue = self.well_known_session_id.Queue()

    client_id = message.source

    # It makes no sense to enrol the same client multiple times, so we
    # eliminate duplicates. Note, that we can still enroll clients multiple
    # times due to cache expiration.
    try:
      enrolment_cache.Get(client_id)
      return
    except KeyError:
      enrolment_cache.Put(client_id, 1)

    # Create a new client object for this client.
    if data_store.AFF4Enabled():
      client = aff4.FACTORY.Create(
          client_id, aff4_grr.VFSGRRClient, mode="rw", token=self.token)
      client_cert = client.Get(client.Schema.CERT)

    if data_store.RelationalDBEnabled():
      try:
        md = data_store.REL_DB.ReadClientMetadata(client_id.Basename())
        client_cert = md.certificate
      except db.UnknownClientError:
        client_cert = None

    if data_store.RelationalDBEnabled():
      data_store.REL_DB.WriteClientMetadata(
          client_id.Basename(), fleetspeak_enabled=False)

    # Only enroll this client if it has no certificate yet.
    if not client_cert:
      # Start the enrollment flow for this client.

      # Note, that the actual CAEnroler class is autogenerated from the
      # CAEnrolerMixin by the DualDBFlow decorator confusing the linter - hence
      # the disable directive.
      flow.StartAFF4Flow(
          client_id=client_id,
          flow_name=CAEnroler.__name__,  # pylint: disable=undefined-variable
          csr=cert,
          queue=queue,
          token=self.token)


class EnrolmentHandler(message_handlers.MessageHandler):
  """Message handler to process enrolment requests."""

  handler_name = "Enrol"

  def ProcessMessages(self, msgs):
    client_ids = set()
    requests = {}

    for msg in msgs:
      client_id = msg.client_id

      # It makes no sense to enrol the same client multiple times, so we
      # eliminate duplicates. Note, that we can still enroll clients multiple
      # times due to cache expiration.
      try:
        enrolment_cache.Get(client_id)
        continue
      except KeyError:
        enrolment_cache.Put(client_id, 1)
      client_ids.add(client_id)
      requests[client_id] = msg.request.payload

    if not client_ids:
      return

    try:
      mds = data_store.REL_DB.MultiReadClientMetadata(list(client_ids))
      for client_id in client_ids:
        if client_id not in mds or not mds[client_id].certificate:
          # Start the enrollment flow for this client.

          # As mentioned in the comment above, the CAEnroler class is
          # autogenerated which confuses the linter.
          if data_store.RelationalDBEnabled():
            data_store.REL_DB.WriteClientMetadata(
                client_id,
                first_seen=rdfvalue.RDFDatetime.Now(),
                fleetspeak_enabled=False)
            flow.StartFlow(
                client_id=client_id,
                flow_cls=CAEnroler,  # pylint: disable=undefined-variable
                creator="GRRWorker",
                csr=requests[client_id])
          else:
            flow.StartAFF4Flow(
                client_id=client_id,
                flow_name=CAEnroler.__name__,  # pylint: disable=undefined-variable
                csr=requests[client_id],
                queue=queues.ENROLLMENT,
                token=self.token)
    except Exception as e:  # pylint: disable=broad-except
      logging.exception("Exception while starting interrogate: %s", e)
