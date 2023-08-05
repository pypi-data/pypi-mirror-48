# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/contrib/tensor_forest/proto/tensor_forest_params.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.contrib.decision_trees.proto import generic_tree_model_pb2 as tensorflow_dot_contrib_dot_decision__trees_dot_proto_dot_generic__tree__model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/contrib/tensor_forest/proto/tensor_forest_params.proto',
  package='tensorflow.tensorforest',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nAtensorflow/contrib/tensor_forest/proto/tensor_forest_params.proto\x12\x17tensorflow.tensorforest\x1a@tensorflow/contrib/decision_trees/proto/generic_tree_model.proto\"\xa0\x01\n\x12SplitPruningConfig\x12I\n\x13prune_every_samples\x18\x01 \x01(\x0b\x32,.tensorflow.tensorforest.DepthDependentParam\x12?\n\x04type\x18\x02 \x01(\x0e\x32\x31.tensorflow.tensorforest.SplitPruningStrategyType\"\x9c\x01\n\x11SplitFinishConfig\x12G\n\x11\x63heck_every_steps\x18\x01 \x01(\x0b\x32,.tensorflow.tensorforest.DepthDependentParam\x12>\n\x04type\x18\x02 \x01(\x0e\x32\x30.tensorflow.tensorforest.SplitFinishStrategyType\"S\n\x0bLinearParam\x12\r\n\x05slope\x18\x01 \x01(\x02\x12\x13\n\x0by_intercept\x18\x02 \x01(\x02\x12\x0f\n\x07min_val\x18\x03 \x01(\x02\x12\x0f\n\x07max_val\x18\x04 \x01(\x02\"\\\n\x10\x45xponentialParam\x12\x0c\n\x04\x62ias\x18\x01 \x01(\x02\x12\x0c\n\x04\x62\x61se\x18\x02 \x01(\x02\x12\x12\n\nmultiplier\x18\x03 \x01(\x02\x12\x18\n\x10\x64\x65pth_multiplier\x18\x04 \x01(\x02\"H\n\x0eThresholdParam\x12\x10\n\x08on_value\x18\x01 \x01(\x02\x12\x11\n\toff_value\x18\x02 \x01(\x02\x12\x11\n\tthreshold\x18\x03 \x01(\x02\"\xf4\x01\n\x13\x44\x65pthDependentParam\x12\x18\n\x0e\x63onstant_value\x18\x01 \x01(\x02H\x00\x12\x36\n\x06linear\x18\x02 \x01(\x0b\x32$.tensorflow.tensorforest.LinearParamH\x00\x12@\n\x0b\x65xponential\x18\x03 \x01(\x0b\x32).tensorflow.tensorforest.ExponentialParamH\x00\x12<\n\tthreshold\x18\x04 \x01(\x0b\x32\'.tensorflow.tensorforest.ThresholdParamH\x00\x42\x0b\n\tParamType\"\xb7\x08\n\x12TensorForestParams\x12\x39\n\tleaf_type\x18\x01 \x01(\x0e\x32&.tensorflow.tensorforest.LeafModelType\x12;\n\nstats_type\x18\x02 \x01(\x0e\x32\'.tensorflow.tensorforest.StatsModelType\x12\x45\n\x0f\x63ollection_type\x18\x03 \x01(\x0e\x32,.tensorflow.tensorforest.SplitCollectionType\x12\x41\n\x0cpruning_type\x18\x04 \x01(\x0b\x32+.tensorflow.tensorforest.SplitPruningConfig\x12?\n\x0b\x66inish_type\x18\x05 \x01(\x0b\x32*.tensorflow.tensorforest.SplitFinishConfig\x12\x11\n\tnum_trees\x18\x06 \x01(\x05\x12\x11\n\tmax_nodes\x18\x07 \x01(\x05\x12\x14\n\x0cnum_features\x18\x15 \x01(\x05\x12L\n\x14inequality_test_type\x18\x13 \x01(\x0e\x32..tensorflow.decision_trees.InequalityTest.Type\x12\x15\n\ris_regression\x18\x08 \x01(\x08\x12\x18\n\x10\x64rop_final_class\x18\t \x01(\x08\x12\x18\n\x10\x63ollate_examples\x18\n \x01(\x08\x12\x18\n\x10\x63heckpoint_stats\x18\x0b \x01(\x08\x12 \n\x18use_running_stats_method\x18\x14 \x01(\x08\x12!\n\x19initialize_average_splits\x18\x16 \x01(\x08\x12\x1c\n\x14inference_tree_paths\x18\x17 \x01(\x08\x12\x13\n\x0bnum_outputs\x18\x0c \x01(\x05\x12L\n\x16num_splits_to_consider\x18\r \x01(\x0b\x32,.tensorflow.tensorforest.DepthDependentParam\x12I\n\x13split_after_samples\x18\x0e \x01(\x0b\x32,.tensorflow.tensorforest.DepthDependentParam\x12G\n\x11\x64ominate_fraction\x18\x0f \x01(\x0b\x32,.tensorflow.tensorforest.DepthDependentParam\x12G\n\x11min_split_samples\x18\x12 \x01(\x0b\x32,.tensorflow.tensorforest.DepthDependentParam\x12\x11\n\tgraph_dir\x18\x10 \x01(\t\x12\x1b\n\x13num_select_features\x18\x11 \x01(\x05\x12\x1c\n\x14num_classes_to_track\x18\x18 \x01(\x05*\x90\x01\n\rLeafModelType\x12\x1e\n\x1aMODEL_DENSE_CLASSIFICATION\x10\x00\x12\x1f\n\x1bMODEL_SPARSE_CLASSIFICATION\x10\x01\x12\x14\n\x10MODEL_REGRESSION\x10\x02\x12(\n$MODEL_SPARSE_OR_DENSE_CLASSIFICATION\x10\x03*\xa5\x01\n\x0eStatsModelType\x12\x14\n\x10STATS_DENSE_GINI\x10\x00\x12\x15\n\x11STATS_SPARSE_GINI\x10\x01\x12\"\n\x1eSTATS_LEAST_SQUARES_REGRESSION\x10\x02\x12 \n\x1cSTATS_SPARSE_THEN_DENSE_GINI\x10\x03\x12 \n\x1cSTATS_FIXED_SIZE_SPARSE_GINI\x10\x04*H\n\x13SplitCollectionType\x12\x14\n\x10\x43OLLECTION_BASIC\x10\x00\x12\x1b\n\x17GRAPH_RUNNER_COLLECTION\x10\x01*\x96\x01\n\x18SplitPruningStrategyType\x12\x14\n\x10SPLIT_PRUNE_NONE\x10\x00\x12\x14\n\x10SPLIT_PRUNE_HALF\x10\x01\x12\x17\n\x13SPLIT_PRUNE_QUARTER\x10\x02\x12\x1a\n\x16SPLIT_PRUNE_10_PERCENT\x10\x03\x12\x19\n\x15SPLIT_PRUNE_HOEFFDING\x10\x04*{\n\x17SplitFinishStrategyType\x12\x16\n\x12SPLIT_FINISH_BASIC\x10\x00\x12#\n\x1fSPLIT_FINISH_DOMINATE_HOEFFDING\x10\x02\x12#\n\x1fSPLIT_FINISH_DOMINATE_BOOTSTRAP\x10\x03\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_contrib_dot_decision__trees_dot_proto_dot_generic__tree__model__pb2.DESCRIPTOR,])

_LEAFMODELTYPE = _descriptor.EnumDescriptor(
  name='LeafModelType',
  full_name='tensorflow.tensorforest.LeafModelType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MODEL_DENSE_CLASSIFICATION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODEL_SPARSE_CLASSIFICATION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODEL_REGRESSION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODEL_SPARSE_OR_DENSE_CLASSIFICATION', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2065,
  serialized_end=2209,
)
_sym_db.RegisterEnumDescriptor(_LEAFMODELTYPE)

LeafModelType = enum_type_wrapper.EnumTypeWrapper(_LEAFMODELTYPE)
_STATSMODELTYPE = _descriptor.EnumDescriptor(
  name='StatsModelType',
  full_name='tensorflow.tensorforest.StatsModelType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATS_DENSE_GINI', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATS_SPARSE_GINI', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATS_LEAST_SQUARES_REGRESSION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATS_SPARSE_THEN_DENSE_GINI', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATS_FIXED_SIZE_SPARSE_GINI', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2212,
  serialized_end=2377,
)
_sym_db.RegisterEnumDescriptor(_STATSMODELTYPE)

StatsModelType = enum_type_wrapper.EnumTypeWrapper(_STATSMODELTYPE)
_SPLITCOLLECTIONTYPE = _descriptor.EnumDescriptor(
  name='SplitCollectionType',
  full_name='tensorflow.tensorforest.SplitCollectionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COLLECTION_BASIC', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAPH_RUNNER_COLLECTION', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2379,
  serialized_end=2451,
)
_sym_db.RegisterEnumDescriptor(_SPLITCOLLECTIONTYPE)

SplitCollectionType = enum_type_wrapper.EnumTypeWrapper(_SPLITCOLLECTIONTYPE)
_SPLITPRUNINGSTRATEGYTYPE = _descriptor.EnumDescriptor(
  name='SplitPruningStrategyType',
  full_name='tensorflow.tensorforest.SplitPruningStrategyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPLIT_PRUNE_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPLIT_PRUNE_HALF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPLIT_PRUNE_QUARTER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPLIT_PRUNE_10_PERCENT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPLIT_PRUNE_HOEFFDING', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2454,
  serialized_end=2604,
)
_sym_db.RegisterEnumDescriptor(_SPLITPRUNINGSTRATEGYTYPE)

SplitPruningStrategyType = enum_type_wrapper.EnumTypeWrapper(_SPLITPRUNINGSTRATEGYTYPE)
_SPLITFINISHSTRATEGYTYPE = _descriptor.EnumDescriptor(
  name='SplitFinishStrategyType',
  full_name='tensorflow.tensorforest.SplitFinishStrategyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SPLIT_FINISH_BASIC', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPLIT_FINISH_DOMINATE_HOEFFDING', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPLIT_FINISH_DOMINATE_BOOTSTRAP', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2606,
  serialized_end=2729,
)
_sym_db.RegisterEnumDescriptor(_SPLITFINISHSTRATEGYTYPE)

SplitFinishStrategyType = enum_type_wrapper.EnumTypeWrapper(_SPLITFINISHSTRATEGYTYPE)
MODEL_DENSE_CLASSIFICATION = 0
MODEL_SPARSE_CLASSIFICATION = 1
MODEL_REGRESSION = 2
MODEL_SPARSE_OR_DENSE_CLASSIFICATION = 3
STATS_DENSE_GINI = 0
STATS_SPARSE_GINI = 1
STATS_LEAST_SQUARES_REGRESSION = 2
STATS_SPARSE_THEN_DENSE_GINI = 3
STATS_FIXED_SIZE_SPARSE_GINI = 4
COLLECTION_BASIC = 0
GRAPH_RUNNER_COLLECTION = 1
SPLIT_PRUNE_NONE = 0
SPLIT_PRUNE_HALF = 1
SPLIT_PRUNE_QUARTER = 2
SPLIT_PRUNE_10_PERCENT = 3
SPLIT_PRUNE_HOEFFDING = 4
SPLIT_FINISH_BASIC = 0
SPLIT_FINISH_DOMINATE_HOEFFDING = 2
SPLIT_FINISH_DOMINATE_BOOTSTRAP = 3



_SPLITPRUNINGCONFIG = _descriptor.Descriptor(
  name='SplitPruningConfig',
  full_name='tensorflow.tensorforest.SplitPruningConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prune_every_samples', full_name='tensorflow.tensorforest.SplitPruningConfig.prune_every_samples', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.tensorforest.SplitPruningConfig.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=161,
  serialized_end=321,
)


_SPLITFINISHCONFIG = _descriptor.Descriptor(
  name='SplitFinishConfig',
  full_name='tensorflow.tensorforest.SplitFinishConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='check_every_steps', full_name='tensorflow.tensorforest.SplitFinishConfig.check_every_steps', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.tensorforest.SplitFinishConfig.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=324,
  serialized_end=480,
)


_LINEARPARAM = _descriptor.Descriptor(
  name='LinearParam',
  full_name='tensorflow.tensorforest.LinearParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slope', full_name='tensorflow.tensorforest.LinearParam.slope', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y_intercept', full_name='tensorflow.tensorforest.LinearParam.y_intercept', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_val', full_name='tensorflow.tensorforest.LinearParam.min_val', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_val', full_name='tensorflow.tensorforest.LinearParam.max_val', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=482,
  serialized_end=565,
)


_EXPONENTIALPARAM = _descriptor.Descriptor(
  name='ExponentialParam',
  full_name='tensorflow.tensorforest.ExponentialParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bias', full_name='tensorflow.tensorforest.ExponentialParam.bias', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base', full_name='tensorflow.tensorforest.ExponentialParam.base', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiplier', full_name='tensorflow.tensorforest.ExponentialParam.multiplier', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth_multiplier', full_name='tensorflow.tensorforest.ExponentialParam.depth_multiplier', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=567,
  serialized_end=659,
)


_THRESHOLDPARAM = _descriptor.Descriptor(
  name='ThresholdParam',
  full_name='tensorflow.tensorforest.ThresholdParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='on_value', full_name='tensorflow.tensorforest.ThresholdParam.on_value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='off_value', full_name='tensorflow.tensorforest.ThresholdParam.off_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='tensorflow.tensorforest.ThresholdParam.threshold', index=2,
      number=3, type=2, cpp_type=6, label=1,
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
  serialized_start=661,
  serialized_end=733,
)


_DEPTHDEPENDENTPARAM = _descriptor.Descriptor(
  name='DepthDependentParam',
  full_name='tensorflow.tensorforest.DepthDependentParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='constant_value', full_name='tensorflow.tensorforest.DepthDependentParam.constant_value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear', full_name='tensorflow.tensorforest.DepthDependentParam.linear', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exponential', full_name='tensorflow.tensorforest.DepthDependentParam.exponential', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='tensorflow.tensorforest.DepthDependentParam.threshold', index=3,
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
    _descriptor.OneofDescriptor(
      name='ParamType', full_name='tensorflow.tensorforest.DepthDependentParam.ParamType',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=736,
  serialized_end=980,
)


_TENSORFORESTPARAMS = _descriptor.Descriptor(
  name='TensorForestParams',
  full_name='tensorflow.tensorforest.TensorForestParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='leaf_type', full_name='tensorflow.tensorforest.TensorForestParams.leaf_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats_type', full_name='tensorflow.tensorforest.TensorForestParams.stats_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_type', full_name='tensorflow.tensorforest.TensorForestParams.collection_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pruning_type', full_name='tensorflow.tensorforest.TensorForestParams.pruning_type', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finish_type', full_name='tensorflow.tensorforest.TensorForestParams.finish_type', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_trees', full_name='tensorflow.tensorforest.TensorForestParams.num_trees', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_nodes', full_name='tensorflow.tensorforest.TensorForestParams.max_nodes', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_features', full_name='tensorflow.tensorforest.TensorForestParams.num_features', index=7,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inequality_test_type', full_name='tensorflow.tensorforest.TensorForestParams.inequality_test_type', index=8,
      number=19, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_regression', full_name='tensorflow.tensorforest.TensorForestParams.is_regression', index=9,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drop_final_class', full_name='tensorflow.tensorforest.TensorForestParams.drop_final_class', index=10,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collate_examples', full_name='tensorflow.tensorforest.TensorForestParams.collate_examples', index=11,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint_stats', full_name='tensorflow.tensorforest.TensorForestParams.checkpoint_stats', index=12,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_running_stats_method', full_name='tensorflow.tensorforest.TensorForestParams.use_running_stats_method', index=13,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initialize_average_splits', full_name='tensorflow.tensorforest.TensorForestParams.initialize_average_splits', index=14,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inference_tree_paths', full_name='tensorflow.tensorforest.TensorForestParams.inference_tree_paths', index=15,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_outputs', full_name='tensorflow.tensorforest.TensorForestParams.num_outputs', index=16,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_splits_to_consider', full_name='tensorflow.tensorforest.TensorForestParams.num_splits_to_consider', index=17,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='split_after_samples', full_name='tensorflow.tensorforest.TensorForestParams.split_after_samples', index=18,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dominate_fraction', full_name='tensorflow.tensorforest.TensorForestParams.dominate_fraction', index=19,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_split_samples', full_name='tensorflow.tensorforest.TensorForestParams.min_split_samples', index=20,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graph_dir', full_name='tensorflow.tensorforest.TensorForestParams.graph_dir', index=21,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_select_features', full_name='tensorflow.tensorforest.TensorForestParams.num_select_features', index=22,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_classes_to_track', full_name='tensorflow.tensorforest.TensorForestParams.num_classes_to_track', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=983,
  serialized_end=2062,
)

_SPLITPRUNINGCONFIG.fields_by_name['prune_every_samples'].message_type = _DEPTHDEPENDENTPARAM
_SPLITPRUNINGCONFIG.fields_by_name['type'].enum_type = _SPLITPRUNINGSTRATEGYTYPE
_SPLITFINISHCONFIG.fields_by_name['check_every_steps'].message_type = _DEPTHDEPENDENTPARAM
_SPLITFINISHCONFIG.fields_by_name['type'].enum_type = _SPLITFINISHSTRATEGYTYPE
_DEPTHDEPENDENTPARAM.fields_by_name['linear'].message_type = _LINEARPARAM
_DEPTHDEPENDENTPARAM.fields_by_name['exponential'].message_type = _EXPONENTIALPARAM
_DEPTHDEPENDENTPARAM.fields_by_name['threshold'].message_type = _THRESHOLDPARAM
_DEPTHDEPENDENTPARAM.oneofs_by_name['ParamType'].fields.append(
  _DEPTHDEPENDENTPARAM.fields_by_name['constant_value'])
_DEPTHDEPENDENTPARAM.fields_by_name['constant_value'].containing_oneof = _DEPTHDEPENDENTPARAM.oneofs_by_name['ParamType']
_DEPTHDEPENDENTPARAM.oneofs_by_name['ParamType'].fields.append(
  _DEPTHDEPENDENTPARAM.fields_by_name['linear'])
_DEPTHDEPENDENTPARAM.fields_by_name['linear'].containing_oneof = _DEPTHDEPENDENTPARAM.oneofs_by_name['ParamType']
_DEPTHDEPENDENTPARAM.oneofs_by_name['ParamType'].fields.append(
  _DEPTHDEPENDENTPARAM.fields_by_name['exponential'])
_DEPTHDEPENDENTPARAM.fields_by_name['exponential'].containing_oneof = _DEPTHDEPENDENTPARAM.oneofs_by_name['ParamType']
_DEPTHDEPENDENTPARAM.oneofs_by_name['ParamType'].fields.append(
  _DEPTHDEPENDENTPARAM.fields_by_name['threshold'])
_DEPTHDEPENDENTPARAM.fields_by_name['threshold'].containing_oneof = _DEPTHDEPENDENTPARAM.oneofs_by_name['ParamType']
_TENSORFORESTPARAMS.fields_by_name['leaf_type'].enum_type = _LEAFMODELTYPE
_TENSORFORESTPARAMS.fields_by_name['stats_type'].enum_type = _STATSMODELTYPE
_TENSORFORESTPARAMS.fields_by_name['collection_type'].enum_type = _SPLITCOLLECTIONTYPE
_TENSORFORESTPARAMS.fields_by_name['pruning_type'].message_type = _SPLITPRUNINGCONFIG
_TENSORFORESTPARAMS.fields_by_name['finish_type'].message_type = _SPLITFINISHCONFIG
_TENSORFORESTPARAMS.fields_by_name['inequality_test_type'].enum_type = tensorflow_dot_contrib_dot_decision__trees_dot_proto_dot_generic__tree__model__pb2._INEQUALITYTEST_TYPE
_TENSORFORESTPARAMS.fields_by_name['num_splits_to_consider'].message_type = _DEPTHDEPENDENTPARAM
_TENSORFORESTPARAMS.fields_by_name['split_after_samples'].message_type = _DEPTHDEPENDENTPARAM
_TENSORFORESTPARAMS.fields_by_name['dominate_fraction'].message_type = _DEPTHDEPENDENTPARAM
_TENSORFORESTPARAMS.fields_by_name['min_split_samples'].message_type = _DEPTHDEPENDENTPARAM
DESCRIPTOR.message_types_by_name['SplitPruningConfig'] = _SPLITPRUNINGCONFIG
DESCRIPTOR.message_types_by_name['SplitFinishConfig'] = _SPLITFINISHCONFIG
DESCRIPTOR.message_types_by_name['LinearParam'] = _LINEARPARAM
DESCRIPTOR.message_types_by_name['ExponentialParam'] = _EXPONENTIALPARAM
DESCRIPTOR.message_types_by_name['ThresholdParam'] = _THRESHOLDPARAM
DESCRIPTOR.message_types_by_name['DepthDependentParam'] = _DEPTHDEPENDENTPARAM
DESCRIPTOR.message_types_by_name['TensorForestParams'] = _TENSORFORESTPARAMS
DESCRIPTOR.enum_types_by_name['LeafModelType'] = _LEAFMODELTYPE
DESCRIPTOR.enum_types_by_name['StatsModelType'] = _STATSMODELTYPE
DESCRIPTOR.enum_types_by_name['SplitCollectionType'] = _SPLITCOLLECTIONTYPE
DESCRIPTOR.enum_types_by_name['SplitPruningStrategyType'] = _SPLITPRUNINGSTRATEGYTYPE
DESCRIPTOR.enum_types_by_name['SplitFinishStrategyType'] = _SPLITFINISHSTRATEGYTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SplitPruningConfig = _reflection.GeneratedProtocolMessageType('SplitPruningConfig', (_message.Message,), dict(
  DESCRIPTOR = _SPLITPRUNINGCONFIG,
  __module__ = 'tensorflow.contrib.tensor_forest.proto.tensor_forest_params_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tensorforest.SplitPruningConfig)
  ))
_sym_db.RegisterMessage(SplitPruningConfig)

SplitFinishConfig = _reflection.GeneratedProtocolMessageType('SplitFinishConfig', (_message.Message,), dict(
  DESCRIPTOR = _SPLITFINISHCONFIG,
  __module__ = 'tensorflow.contrib.tensor_forest.proto.tensor_forest_params_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tensorforest.SplitFinishConfig)
  ))
_sym_db.RegisterMessage(SplitFinishConfig)

LinearParam = _reflection.GeneratedProtocolMessageType('LinearParam', (_message.Message,), dict(
  DESCRIPTOR = _LINEARPARAM,
  __module__ = 'tensorflow.contrib.tensor_forest.proto.tensor_forest_params_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tensorforest.LinearParam)
  ))
_sym_db.RegisterMessage(LinearParam)

ExponentialParam = _reflection.GeneratedProtocolMessageType('ExponentialParam', (_message.Message,), dict(
  DESCRIPTOR = _EXPONENTIALPARAM,
  __module__ = 'tensorflow.contrib.tensor_forest.proto.tensor_forest_params_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tensorforest.ExponentialParam)
  ))
_sym_db.RegisterMessage(ExponentialParam)

ThresholdParam = _reflection.GeneratedProtocolMessageType('ThresholdParam', (_message.Message,), dict(
  DESCRIPTOR = _THRESHOLDPARAM,
  __module__ = 'tensorflow.contrib.tensor_forest.proto.tensor_forest_params_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tensorforest.ThresholdParam)
  ))
_sym_db.RegisterMessage(ThresholdParam)

DepthDependentParam = _reflection.GeneratedProtocolMessageType('DepthDependentParam', (_message.Message,), dict(
  DESCRIPTOR = _DEPTHDEPENDENTPARAM,
  __module__ = 'tensorflow.contrib.tensor_forest.proto.tensor_forest_params_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tensorforest.DepthDependentParam)
  ))
_sym_db.RegisterMessage(DepthDependentParam)

TensorForestParams = _reflection.GeneratedProtocolMessageType('TensorForestParams', (_message.Message,), dict(
  DESCRIPTOR = _TENSORFORESTPARAMS,
  __module__ = 'tensorflow.contrib.tensor_forest.proto.tensor_forest_params_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tensorforest.TensorForestParams)
  ))
_sym_db.RegisterMessage(TensorForestParams)


# @@protoc_insertion_point(module_scope)
