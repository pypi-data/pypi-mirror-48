# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""SavedModel builder.

Builds a SavedModel that can be saved to storage, is language neutral, and
enables systems to produce, consume, or transform TensorFlow Models.


"""

from __future__ import print_function as _print_function

from tensorflow.python.saved_model.builder import SavedModelBuilder

del _print_function

import sys as _sys
from tensorflow.python.util import deprecation_wrapper as _deprecation_wrapper

if not isinstance(_sys.modules[__name__], _deprecation_wrapper.DeprecationWrapper):
  _sys.modules[__name__] = _deprecation_wrapper.DeprecationWrapper(
      _sys.modules[__name__], "saved_model.builder")
