# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/contrib/rpc/python/kernel_tests/test_example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/contrib/rpc/python/kernel_tests/test_example.proto',
  package='tensorflow.contrib.rpc',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n=tensorflow/contrib/rpc/python/kernel_tests/test_example.proto\x12\x16tensorflow.contrib.rpc\"\x1a\n\x08TestCase\x12\x0e\n\x06values\x18\x01 \x03(\x05\x32\xea\x03\n\x0fTestCaseService\x12Q\n\tIncrement\x12 .tensorflow.contrib.rpc.TestCase\x1a .tensorflow.contrib.rpc.TestCase\"\x00\x12T\n\x0cSleepForever\x12 .tensorflow.contrib.rpc.TestCase\x1a .tensorflow.contrib.rpc.TestCase\"\x00\x12]\n\x15SometimesSleepForever\x12 .tensorflow.contrib.rpc.TestCase\x1a .tensorflow.contrib.rpc.TestCase\"\x00\x12\x65\n\x1d\x41lwaysFailWithInvalidArgument\x12 .tensorflow.contrib.rpc.TestCase\x1a .tensorflow.contrib.rpc.TestCase\"\x00\x12h\n SometimesFailWithInvalidArgument\x12 .tensorflow.contrib.rpc.TestCase\x1a .tensorflow.contrib.rpc.TestCase\"\x00')
)




_TESTCASE = _descriptor.Descriptor(
  name='TestCase',
  full_name='tensorflow.contrib.rpc.TestCase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='tensorflow.contrib.rpc.TestCase.values', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['TestCase'] = _TESTCASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestCase = _reflection.GeneratedProtocolMessageType('TestCase', (_message.Message,), dict(
  DESCRIPTOR = _TESTCASE,
  __module__ = 'tensorflow.contrib.rpc.python.kernel_tests.test_example_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.contrib.rpc.TestCase)
  ))
_sym_db.RegisterMessage(TestCase)



_TESTCASESERVICE = _descriptor.ServiceDescriptor(
  name='TestCaseService',
  full_name='tensorflow.contrib.rpc.TestCaseService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=118,
  serialized_end=608,
  methods=[
  _descriptor.MethodDescriptor(
    name='Increment',
    full_name='tensorflow.contrib.rpc.TestCaseService.Increment',
    index=0,
    containing_service=None,
    input_type=_TESTCASE,
    output_type=_TESTCASE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SleepForever',
    full_name='tensorflow.contrib.rpc.TestCaseService.SleepForever',
    index=1,
    containing_service=None,
    input_type=_TESTCASE,
    output_type=_TESTCASE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SometimesSleepForever',
    full_name='tensorflow.contrib.rpc.TestCaseService.SometimesSleepForever',
    index=2,
    containing_service=None,
    input_type=_TESTCASE,
    output_type=_TESTCASE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AlwaysFailWithInvalidArgument',
    full_name='tensorflow.contrib.rpc.TestCaseService.AlwaysFailWithInvalidArgument',
    index=3,
    containing_service=None,
    input_type=_TESTCASE,
    output_type=_TESTCASE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SometimesFailWithInvalidArgument',
    full_name='tensorflow.contrib.rpc.TestCaseService.SometimesFailWithInvalidArgument',
    index=4,
    containing_service=None,
    input_type=_TESTCASE,
    output_type=_TESTCASE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTCASESERVICE)

DESCRIPTOR.services_by_name['TestCaseService'] = _TESTCASESERVICE

# @@protoc_insertion_point(module_scope)
