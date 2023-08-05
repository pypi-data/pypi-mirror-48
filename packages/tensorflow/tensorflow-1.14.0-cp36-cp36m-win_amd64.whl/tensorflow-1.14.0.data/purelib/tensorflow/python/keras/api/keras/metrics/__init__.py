# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Built-in metrics.

"""

from __future__ import print_function as _print_function

from tensorflow.python.keras.losses import KLD
from tensorflow.python.keras.losses import KLD as kld
from tensorflow.python.keras.losses import KLD as kullback_leibler_divergence
from tensorflow.python.keras.losses import MAE
from tensorflow.python.keras.losses import MAE as mae
from tensorflow.python.keras.losses import MAE as mean_absolute_error
from tensorflow.python.keras.losses import MAPE
from tensorflow.python.keras.losses import MAPE as mape
from tensorflow.python.keras.losses import MAPE as mean_absolute_percentage_error
from tensorflow.python.keras.losses import MSE
from tensorflow.python.keras.losses import MSE as mean_squared_error
from tensorflow.python.keras.losses import MSE as mse
from tensorflow.python.keras.losses import MSLE
from tensorflow.python.keras.losses import MSLE as mean_squared_logarithmic_error
from tensorflow.python.keras.losses import MSLE as msle
from tensorflow.python.keras.losses import binary_crossentropy
from tensorflow.python.keras.losses import categorical_crossentropy
from tensorflow.python.keras.losses import cosine_proximity
from tensorflow.python.keras.losses import cosine_proximity as cosine
from tensorflow.python.keras.losses import hinge
from tensorflow.python.keras.losses import poisson
from tensorflow.python.keras.losses import sparse_categorical_crossentropy
from tensorflow.python.keras.losses import squared_hinge
from tensorflow.python.keras.metrics import AUC
from tensorflow.python.keras.metrics import Accuracy
from tensorflow.python.keras.metrics import BinaryAccuracy
from tensorflow.python.keras.metrics import BinaryCrossentropy
from tensorflow.python.keras.metrics import CategoricalAccuracy
from tensorflow.python.keras.metrics import CategoricalCrossentropy
from tensorflow.python.keras.metrics import CategoricalHinge
from tensorflow.python.keras.metrics import CosineSimilarity
from tensorflow.python.keras.metrics import FalseNegatives
from tensorflow.python.keras.metrics import FalsePositives
from tensorflow.python.keras.metrics import Hinge
from tensorflow.python.keras.metrics import KLDivergence
from tensorflow.python.keras.metrics import LogCoshError
from tensorflow.python.keras.metrics import Mean
from tensorflow.python.keras.metrics import MeanAbsoluteError
from tensorflow.python.keras.metrics import MeanAbsolutePercentageError
from tensorflow.python.keras.metrics import MeanIoU
from tensorflow.python.keras.metrics import MeanRelativeError
from tensorflow.python.keras.metrics import MeanSquaredError
from tensorflow.python.keras.metrics import MeanSquaredLogarithmicError
from tensorflow.python.keras.metrics import MeanTensor
from tensorflow.python.keras.metrics import Metric
from tensorflow.python.keras.metrics import Poisson
from tensorflow.python.keras.metrics import Precision
from tensorflow.python.keras.metrics import Recall
from tensorflow.python.keras.metrics import RootMeanSquaredError
from tensorflow.python.keras.metrics import SensitivityAtSpecificity
from tensorflow.python.keras.metrics import SparseCategoricalAccuracy
from tensorflow.python.keras.metrics import SparseCategoricalCrossentropy
from tensorflow.python.keras.metrics import SparseTopKCategoricalAccuracy
from tensorflow.python.keras.metrics import SpecificityAtSensitivity
from tensorflow.python.keras.metrics import SquaredHinge
from tensorflow.python.keras.metrics import Sum
from tensorflow.python.keras.metrics import TopKCategoricalAccuracy
from tensorflow.python.keras.metrics import TrueNegatives
from tensorflow.python.keras.metrics import TruePositives
from tensorflow.python.keras.metrics import binary_accuracy
from tensorflow.python.keras.metrics import categorical_accuracy
from tensorflow.python.keras.metrics import deserialize
from tensorflow.python.keras.metrics import get
from tensorflow.python.keras.metrics import serialize
from tensorflow.python.keras.metrics import sparse_categorical_accuracy
from tensorflow.python.keras.metrics import sparse_top_k_categorical_accuracy
from tensorflow.python.keras.metrics import top_k_categorical_accuracy

del _print_function

import sys as _sys
from tensorflow.python.util import deprecation_wrapper as _deprecation_wrapper

if not isinstance(_sys.modules[__name__], _deprecation_wrapper.DeprecationWrapper):
  _sys.modules[__name__] = _deprecation_wrapper.DeprecationWrapper(
      _sys.modules[__name__], "keras.metrics")
