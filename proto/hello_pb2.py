# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bhello.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t23\n\x07Greeter\x12(\n\x08SayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00\x42\nZ\x08../protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\010../proto'
  _globals['_HELLOREQUEST']._serialized_start=15
  _globals['_HELLOREQUEST']._serialized_end=43
  _globals['_HELLOREPLY']._serialized_start=45
  _globals['_HELLOREPLY']._serialized_end=74
  _globals['_GREETER']._serialized_start=76
  _globals['_GREETER']._serialized_end=127
# @@protoc_insertion_point(module_scope)
