# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Keras initializer serialization / deserialization.

"""

from __future__ import print_function as _print_function

from tensorflow.python import Constant
from tensorflow.python import Constant as constant
from tensorflow.python import GlorotNormal as glorot_normal
from tensorflow.python import GlorotUniform as glorot_uniform
from tensorflow.python import Identity
from tensorflow.python import Identity as identity
from tensorflow.python import Initializer
from tensorflow.python import Ones
from tensorflow.python import Ones as ones
from tensorflow.python import Orthogonal
from tensorflow.python import Orthogonal as orthogonal
from tensorflow.python import VarianceScaling
from tensorflow.python import Zeros
from tensorflow.python import Zeros as zeros
from tensorflow.python import he_normal
from tensorflow.python import he_uniform
from tensorflow.python import lecun_normal
from tensorflow.python import lecun_uniform
from tensorflow.python.keras.initializers import RandomNormal
from tensorflow.python.keras.initializers import RandomNormal as normal
from tensorflow.python.keras.initializers import RandomNormal as random_normal
from tensorflow.python.keras.initializers import RandomUniform
from tensorflow.python.keras.initializers import RandomUniform as random_uniform
from tensorflow.python.keras.initializers import RandomUniform as uniform
from tensorflow.python.keras.initializers import TruncatedNormal
from tensorflow.python.keras.initializers import TruncatedNormal as truncated_normal
from tensorflow.python.keras.initializers import deserialize
from tensorflow.python.keras.initializers import get
from tensorflow.python.keras.initializers import serialize

del _print_function

import sys as _sys
from tensorflow.python.util import deprecation_wrapper as _deprecation_wrapper

if not isinstance(_sys.modules[__name__], _deprecation_wrapper.DeprecationWrapper):
  _sys.modules[__name__] = _deprecation_wrapper.DeprecationWrapper(
      _sys.modules[__name__], "keras.initializers")
