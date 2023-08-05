# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Experimental Distribution Strategy library.
"""

from __future__ import print_function as _print_function

from tensorflow.python.distribute.central_storage_strategy import CentralStorageStrategyV1 as CentralStorageStrategy
from tensorflow.python.distribute.collective_all_reduce_strategy import CollectiveAllReduceStrategyV1 as MultiWorkerMirroredStrategy
from tensorflow.python.distribute.cross_device_ops import CollectiveCommunication
from tensorflow.python.distribute.parameter_server_strategy import ParameterServerStrategyV1 as ParameterServerStrategy
from tensorflow.python.distribute.tpu_strategy import TPUStrategyV1 as TPUStrategy

del _print_function

import sys as _sys
from tensorflow.python.util import deprecation_wrapper as _deprecation_wrapper

if not isinstance(_sys.modules[__name__], _deprecation_wrapper.DeprecationWrapper):
  _sys.modules[__name__] = _deprecation_wrapper.DeprecationWrapper(
      _sys.modules[__name__], "distribute.experimental")
