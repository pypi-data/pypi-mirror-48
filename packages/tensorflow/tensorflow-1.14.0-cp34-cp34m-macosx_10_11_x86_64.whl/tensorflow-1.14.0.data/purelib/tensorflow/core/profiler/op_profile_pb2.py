# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/profiler/op_profile.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/profiler/op_profile.proto',
  package='tensorflow.profiler.op_profile',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n)tensorflow/core/profiler/op_profile.proto\x12\x1etensorflow.profiler.op_profile\"\xad\x01\n\x07Profile\x12\x39\n\x0b\x62y_category\x18\x01 \x01(\x0b\x32$.tensorflow.profiler.op_profile.Node\x12\x38\n\nby_program\x18\x04 \x01(\x0b\x32$.tensorflow.profiler.op_profile.NodeJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04R\x14\x62y_program_structureR\x0bper_program\"\xb4\x05\n\x04Node\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\x07metrics\x18\x02 \x01(\x0b\x32\'.tensorflow.profiler.op_profile.Metrics\x12\x36\n\x08\x63hildren\x18\x03 \x03(\x0b\x32$.tensorflow.profiler.op_profile.Node\x12L\n\x08\x63\x61tegory\x18\x04 \x01(\x0b\x32\x38.tensorflow.profiler.op_profile.Node.InstructionCategoryH\x00\x12\x42\n\x03xla\x18\x05 \x01(\x0b\x32\x33.tensorflow.profiler.op_profile.Node.XLAInstructionH\x00\x12\x14\n\x0cnum_children\x18\x06 \x01(\x05\x1a\x15\n\x13InstructionCategory\x1a\xe0\x02\n\x0eXLAInstruction\x12\n\n\x02op\x18\x01 \x01(\t\x12\x12\n\nexpression\x18\x02 \x01(\t\x12\x12\n\nprovenance\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12R\n\x06layout\x18\x05 \x01(\x0b\x32\x42.tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis\x1a\xb3\x01\n\x0eLayoutAnalysis\x12`\n\ndimensions\x18\x01 \x03(\x0b\x32L.tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.Dimension\x1a?\n\tDimension\x12\x0c\n\x04size\x18\x01 \x01(\x05\x12\x11\n\talignment\x18\x02 \x01(\x05\x12\x11\n\tsemantics\x18\x03 \x01(\tB\n\n\x08\x63ontents\"\x81\x01\n\x07Metrics\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\r\n\x05\x66lops\x18\x02 \x01(\x01\x12\x18\n\x10memory_bandwidth\x18\x03 \x01(\x01\x12\x10\n\x08raw_time\x18\x0b \x01(\x01\x12\x11\n\traw_flops\x18\x0c \x01(\x01\x12\x1a\n\x12raw_bytes_accessed\x18\r \x01(\x01\x62\x06proto3')
)




_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='tensorflow.profiler.op_profile.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='by_category', full_name='tensorflow.profiler.op_profile.Profile.by_category', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_program', full_name='tensorflow.profiler.op_profile.Profile.by_program', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=251,
)


_NODE_INSTRUCTIONCATEGORY = _descriptor.Descriptor(
  name='InstructionCategory',
  full_name='tensorflow.profiler.op_profile.Node.InstructionCategory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=558,
  serialized_end=579,
)

_NODE_XLAINSTRUCTION_LAYOUTANALYSIS_DIMENSION = _descriptor.Descriptor(
  name='Dimension',
  full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.Dimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.Dimension.size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alignment', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.Dimension.alignment', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='semantics', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.Dimension.semantics', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=871,
  serialized_end=934,
)

_NODE_XLAINSTRUCTION_LAYOUTANALYSIS = _descriptor.Descriptor(
  name='LayoutAnalysis',
  full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.dimensions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NODE_XLAINSTRUCTION_LAYOUTANALYSIS_DIMENSION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=755,
  serialized_end=934,
)

_NODE_XLAINSTRUCTION = _descriptor.Descriptor(
  name='XLAInstruction',
  full_name='tensorflow.profiler.op_profile.Node.XLAInstruction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.op', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expression', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.expression', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provenance', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.provenance', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layout', full_name='tensorflow.profiler.op_profile.Node.XLAInstruction.layout', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NODE_XLAINSTRUCTION_LAYOUTANALYSIS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=582,
  serialized_end=934,
)

_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='tensorflow.profiler.op_profile.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.profiler.op_profile.Node.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='tensorflow.profiler.op_profile.Node.metrics', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='children', full_name='tensorflow.profiler.op_profile.Node.children', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='tensorflow.profiler.op_profile.Node.category', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xla', full_name='tensorflow.profiler.op_profile.Node.xla', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_children', full_name='tensorflow.profiler.op_profile.Node.num_children', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NODE_INSTRUCTIONCATEGORY, _NODE_XLAINSTRUCTION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='contents', full_name='tensorflow.profiler.op_profile.Node.contents',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=254,
  serialized_end=946,
)


_METRICS = _descriptor.Descriptor(
  name='Metrics',
  full_name='tensorflow.profiler.op_profile.Metrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='tensorflow.profiler.op_profile.Metrics.time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flops', full_name='tensorflow.profiler.op_profile.Metrics.flops', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory_bandwidth', full_name='tensorflow.profiler.op_profile.Metrics.memory_bandwidth', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_time', full_name='tensorflow.profiler.op_profile.Metrics.raw_time', index=3,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_flops', full_name='tensorflow.profiler.op_profile.Metrics.raw_flops', index=4,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_bytes_accessed', full_name='tensorflow.profiler.op_profile.Metrics.raw_bytes_accessed', index=5,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=949,
  serialized_end=1078,
)

_PROFILE.fields_by_name['by_category'].message_type = _NODE
_PROFILE.fields_by_name['by_program'].message_type = _NODE
_NODE_INSTRUCTIONCATEGORY.containing_type = _NODE
_NODE_XLAINSTRUCTION_LAYOUTANALYSIS_DIMENSION.containing_type = _NODE_XLAINSTRUCTION_LAYOUTANALYSIS
_NODE_XLAINSTRUCTION_LAYOUTANALYSIS.fields_by_name['dimensions'].message_type = _NODE_XLAINSTRUCTION_LAYOUTANALYSIS_DIMENSION
_NODE_XLAINSTRUCTION_LAYOUTANALYSIS.containing_type = _NODE_XLAINSTRUCTION
_NODE_XLAINSTRUCTION.fields_by_name['layout'].message_type = _NODE_XLAINSTRUCTION_LAYOUTANALYSIS
_NODE_XLAINSTRUCTION.containing_type = _NODE
_NODE.fields_by_name['metrics'].message_type = _METRICS
_NODE.fields_by_name['children'].message_type = _NODE
_NODE.fields_by_name['category'].message_type = _NODE_INSTRUCTIONCATEGORY
_NODE.fields_by_name['xla'].message_type = _NODE_XLAINSTRUCTION
_NODE.oneofs_by_name['contents'].fields.append(
  _NODE.fields_by_name['category'])
_NODE.fields_by_name['category'].containing_oneof = _NODE.oneofs_by_name['contents']
_NODE.oneofs_by_name['contents'].fields.append(
  _NODE.fields_by_name['xla'])
_NODE.fields_by_name['xla'].containing_oneof = _NODE.oneofs_by_name['contents']
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Metrics'] = _METRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), dict(
  DESCRIPTOR = _PROFILE,
  __module__ = 'tensorflow.core.profiler.op_profile_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.op_profile.Profile)
  ))
_sym_db.RegisterMessage(Profile)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(

  InstructionCategory = _reflection.GeneratedProtocolMessageType('InstructionCategory', (_message.Message,), dict(
    DESCRIPTOR = _NODE_INSTRUCTIONCATEGORY,
    __module__ = 'tensorflow.core.profiler.op_profile_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.profiler.op_profile.Node.InstructionCategory)
    ))
  ,

  XLAInstruction = _reflection.GeneratedProtocolMessageType('XLAInstruction', (_message.Message,), dict(

    LayoutAnalysis = _reflection.GeneratedProtocolMessageType('LayoutAnalysis', (_message.Message,), dict(

      Dimension = _reflection.GeneratedProtocolMessageType('Dimension', (_message.Message,), dict(
        DESCRIPTOR = _NODE_XLAINSTRUCTION_LAYOUTANALYSIS_DIMENSION,
        __module__ = 'tensorflow.core.profiler.op_profile_pb2'
        # @@protoc_insertion_point(class_scope:tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis.Dimension)
        ))
      ,
      DESCRIPTOR = _NODE_XLAINSTRUCTION_LAYOUTANALYSIS,
      __module__ = 'tensorflow.core.profiler.op_profile_pb2'
      # @@protoc_insertion_point(class_scope:tensorflow.profiler.op_profile.Node.XLAInstruction.LayoutAnalysis)
      ))
    ,
    DESCRIPTOR = _NODE_XLAINSTRUCTION,
    __module__ = 'tensorflow.core.profiler.op_profile_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.profiler.op_profile.Node.XLAInstruction)
    ))
  ,
  DESCRIPTOR = _NODE,
  __module__ = 'tensorflow.core.profiler.op_profile_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.op_profile.Node)
  ))
_sym_db.RegisterMessage(Node)
_sym_db.RegisterMessage(Node.InstructionCategory)
_sym_db.RegisterMessage(Node.XLAInstruction)
_sym_db.RegisterMessage(Node.XLAInstruction.LayoutAnalysis)
_sym_db.RegisterMessage(Node.XLAInstruction.LayoutAnalysis.Dimension)

Metrics = _reflection.GeneratedProtocolMessageType('Metrics', (_message.Message,), dict(
  DESCRIPTOR = _METRICS,
  __module__ = 'tensorflow.core.profiler.op_profile_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.op_profile.Metrics)
  ))
_sym_db.RegisterMessage(Metrics)


# @@protoc_insertion_point(module_scope)
