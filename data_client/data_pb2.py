# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndata.proto\x12\x04\x44\x61ta\"#\n\x0b\x44\x61taRequest\x12\x14\n\x0clambda_arriv\x18\x01 \x01(\x02\"C\n\x0c\x44\x61taResponse\x12\x0c\n\x04time\x18\x01 \x01(\t\x12\x14\n\x0cinterarrival\x18\x02 \x01(\x01\x12\x0f\n\x07service\x18\x03 \x01(\t2E\n\nDataStream\x12\x37\n\nStreamData\x12\x11.Data.DataRequest\x1a\x12.Data.DataResponse\"\x00\x30\x01\x62\x06proto3')



_DATAREQUEST = DESCRIPTOR.message_types_by_name['DataRequest']
_DATARESPONSE = DESCRIPTOR.message_types_by_name['DataResponse']
DataRequest = _reflection.GeneratedProtocolMessageType('DataRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATAREQUEST,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:Data.DataRequest)
  })
_sym_db.RegisterMessage(DataRequest)

DataResponse = _reflection.GeneratedProtocolMessageType('DataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATARESPONSE,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:Data.DataResponse)
  })
_sym_db.RegisterMessage(DataResponse)

_DATASTREAM = DESCRIPTOR.services_by_name['DataStream']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATAREQUEST._serialized_start=20
  _DATAREQUEST._serialized_end=55
  _DATARESPONSE._serialized_start=57
  _DATARESPONSE._serialized_end=124
  _DATASTREAM._serialized_start=126
  _DATASTREAM._serialized_end=195
# @@protoc_insertion_point(module_scope)
