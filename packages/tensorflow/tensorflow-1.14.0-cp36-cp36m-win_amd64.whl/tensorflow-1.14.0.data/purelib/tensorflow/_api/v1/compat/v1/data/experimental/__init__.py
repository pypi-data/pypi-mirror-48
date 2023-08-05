# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Experimental API for building input pipelines.

This module contains experimental `Dataset` sources and transformations that can
be used in conjunction with the `tf.data.Dataset` API. Note that the
`tf.data.experimental` API is not subject to the same backwards compatibility
guarantees as `tf.data`, but we will provide deprecation advice in advance of
removing existing functionality.

See [Importing Data](https://tensorflow.org/guide/datasets) for an overview.

@@Counter
@@CheckpointInputPipelineHook
@@CsvDataset
@@DatasetStructure
@@DistributeOptions
@@MapVectorizationOptions
@@NestedStructure
@@OptimizationOptions
@@Optional
@@OptionalStructure
@@RaggedTensorStructure
@@RandomDataset
@@Reducer
@@SparseTensorStructure
@@SqlDataset
@@StatsAggregator
@@StatsOptions
@@Structure
@@TFRecordWriter
@@TensorArrayStructure
@@TensorStructure
@@ThreadingOptions

@@bucket_by_sequence_length
@@bytes_produced_stats
@@cardinality
@@choose_from_datasets
@@copy_to_device
@@dense_to_sparse_batch
@@enumerate_dataset
@@from_variant
@@get_next_as_optional
@@get_single_element
@@get_structure
@@group_by_reducer
@@group_by_window
@@ignore_errors
@@latency_stats
@@make_batched_features_dataset
@@make_csv_dataset
@@make_saveable_from_iterator
@@map_and_batch
@@map_and_batch_with_legacy_function
@@parallel_interleave
@@parse_example_dataset
@@prefetch_to_device
@@rejection_resample
@@sample_from_datasets
@@scan
@@shuffle_and_repeat
@@take_while
@@to_variant
@@unbatch
@@unique

@@AUTOTUNE
@@INFINITE_CARDINALITY
@@UNKNOWN_CARDINALITY

"""

from __future__ import print_function as _print_function

from tensorflow.python.data.experimental import CheckpointInputPipelineHook
from tensorflow.python.data.experimental import Counter
from tensorflow.python.data.experimental import CsvDataset
from tensorflow.python.data.experimental import DatasetStructure
from tensorflow.python.data.experimental import DistributeOptions
from tensorflow.python.data.experimental import MapVectorizationOptions
from tensorflow.python.data.experimental import NestedStructure
from tensorflow.python.data.experimental import OptimizationOptions
from tensorflow.python.data.experimental import Optional
from tensorflow.python.data.experimental import OptionalStructure
from tensorflow.python.data.experimental import RaggedTensorStructure
from tensorflow.python.data.experimental import RandomDataset
from tensorflow.python.data.experimental import Reducer
from tensorflow.python.data.experimental import SparseTensorStructure
from tensorflow.python.data.experimental import SqlDataset
from tensorflow.python.data.experimental import StatsAggregator
from tensorflow.python.data.experimental import StatsOptions
from tensorflow.python.data.experimental import Structure
from tensorflow.python.data.experimental import TFRecordWriter
from tensorflow.python.data.experimental import TensorArrayStructure
from tensorflow.python.data.experimental import TensorStructure
from tensorflow.python.data.experimental import ThreadingOptions
from tensorflow.python.data.experimental import bucket_by_sequence_length
from tensorflow.python.data.experimental import bytes_produced_stats
from tensorflow.python.data.experimental import cardinality
from tensorflow.python.data.experimental import choose_from_datasets
from tensorflow.python.data.experimental import copy_to_device
from tensorflow.python.data.experimental import dense_to_sparse_batch
from tensorflow.python.data.experimental import enumerate_dataset
from tensorflow.python.data.experimental import from_variant
from tensorflow.python.data.experimental import get_next_as_optional
from tensorflow.python.data.experimental import get_single_element
from tensorflow.python.data.experimental import get_structure
from tensorflow.python.data.experimental import group_by_reducer
from tensorflow.python.data.experimental import group_by_window
from tensorflow.python.data.experimental import ignore_errors
from tensorflow.python.data.experimental import latency_stats
from tensorflow.python.data.experimental import make_batched_features_dataset
from tensorflow.python.data.experimental import make_csv_dataset
from tensorflow.python.data.experimental import make_saveable_from_iterator
from tensorflow.python.data.experimental import map_and_batch
from tensorflow.python.data.experimental import map_and_batch_with_legacy_function
from tensorflow.python.data.experimental import parallel_interleave
from tensorflow.python.data.experimental import parse_example_dataset
from tensorflow.python.data.experimental import prefetch_to_device
from tensorflow.python.data.experimental import rejection_resample
from tensorflow.python.data.experimental import sample_from_datasets
from tensorflow.python.data.experimental import scan
from tensorflow.python.data.experimental import shuffle_and_repeat
from tensorflow.python.data.experimental import take_while
from tensorflow.python.data.experimental import to_variant
from tensorflow.python.data.experimental import unbatch
from tensorflow.python.data.experimental import unique
from tensorflow.python.data.experimental.ops.cardinality import INFINITE as INFINITE_CARDINALITY
from tensorflow.python.data.experimental.ops.cardinality import UNKNOWN as UNKNOWN_CARDINALITY
from tensorflow.python.data.experimental.ops.optimization import AUTOTUNE

del _print_function
