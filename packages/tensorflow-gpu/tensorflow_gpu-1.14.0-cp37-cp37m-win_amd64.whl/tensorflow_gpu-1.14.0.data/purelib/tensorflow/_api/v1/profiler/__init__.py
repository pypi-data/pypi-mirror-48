# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Public API for tf.profiler namespace.
"""

from __future__ import print_function as _print_function

from tensorflow.python.profiler.model_analyzer import Profiler
from tensorflow.python.profiler.model_analyzer import advise
from tensorflow.python.profiler.model_analyzer import profile
from tensorflow.python.profiler.option_builder import ProfileOptionBuilder
from tensorflow.python.profiler.profiler import AdviceProto
from tensorflow.python.profiler.profiler import GraphNodeProto
from tensorflow.python.profiler.profiler import MultiGraphNodeProto
from tensorflow.python.profiler.profiler import OpLogProto
from tensorflow.python.profiler.profiler import write_op_log

del _print_function

import sys as _sys
from tensorflow.python.util import deprecation_wrapper as _deprecation_wrapper

if not isinstance(_sys.modules[__name__], _deprecation_wrapper.DeprecationWrapper):
  _sys.modules[__name__] = _deprecation_wrapper.DeprecationWrapper(
      _sys.modules[__name__], "profiler")
