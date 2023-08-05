# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Keras layers API.
"""

from __future__ import print_function as _print_function

from tensorflow.python.feature_column.feature_column_lib import DenseFeatures
from tensorflow.python.feature_column.feature_column_lib import Layer
from tensorflow.python.keras import Input
from tensorflow.python.keras.engine import InputLayer
from tensorflow.python.keras.engine import InputSpec
from tensorflow.python.keras.layers import AbstractRNNCell
from tensorflow.python.keras.layers import Activation
from tensorflow.python.keras.layers import ActivityRegularization
from tensorflow.python.keras.layers import Add
from tensorflow.python.keras.layers import AdditiveAttention
from tensorflow.python.keras.layers import AlphaDropout
from tensorflow.python.keras.layers import Attention
from tensorflow.python.keras.layers import Average
from tensorflow.python.keras.layers import AveragePooling1D
from tensorflow.python.keras.layers import AveragePooling1D as AvgPool1D
from tensorflow.python.keras.layers import AveragePooling2D
from tensorflow.python.keras.layers import AveragePooling2D as AvgPool2D
from tensorflow.python.keras.layers import AveragePooling3D
from tensorflow.python.keras.layers import AveragePooling3D as AvgPool3D
from tensorflow.python.keras.layers import BatchNormalization
from tensorflow.python.keras.layers import Bidirectional
from tensorflow.python.keras.layers import Concatenate
from tensorflow.python.keras.layers import Conv1D
from tensorflow.python.keras.layers import Conv1D as Convolution1D
from tensorflow.python.keras.layers import Conv2D
from tensorflow.python.keras.layers import Conv2D as Convolution2D
from tensorflow.python.keras.layers import Conv2DTranspose
from tensorflow.python.keras.layers import Conv2DTranspose as Convolution2DTranspose
from tensorflow.python.keras.layers import Conv3D
from tensorflow.python.keras.layers import Conv3D as Convolution3D
from tensorflow.python.keras.layers import Conv3DTranspose
from tensorflow.python.keras.layers import Conv3DTranspose as Convolution3DTranspose
from tensorflow.python.keras.layers import ConvLSTM2D
from tensorflow.python.keras.layers import Cropping1D
from tensorflow.python.keras.layers import Cropping2D
from tensorflow.python.keras.layers import Cropping3D
from tensorflow.python.keras.layers import CuDNNGRU
from tensorflow.python.keras.layers import CuDNNLSTM
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import DepthwiseConv2D
from tensorflow.python.keras.layers import Dot
from tensorflow.python.keras.layers import Dropout
from tensorflow.python.keras.layers import ELU
from tensorflow.python.keras.layers import Embedding
from tensorflow.python.keras.layers import Flatten
from tensorflow.python.keras.layers import GRU
from tensorflow.python.keras.layers import GRUCell
from tensorflow.python.keras.layers import GaussianDropout
from tensorflow.python.keras.layers import GaussianNoise
from tensorflow.python.keras.layers import GlobalAveragePooling1D
from tensorflow.python.keras.layers import GlobalAveragePooling1D as GlobalAvgPool1D
from tensorflow.python.keras.layers import GlobalAveragePooling2D
from tensorflow.python.keras.layers import GlobalAveragePooling2D as GlobalAvgPool2D
from tensorflow.python.keras.layers import GlobalAveragePooling3D
from tensorflow.python.keras.layers import GlobalAveragePooling3D as GlobalAvgPool3D
from tensorflow.python.keras.layers import GlobalMaxPool1D
from tensorflow.python.keras.layers import GlobalMaxPool1D as GlobalMaxPooling1D
from tensorflow.python.keras.layers import GlobalMaxPool2D
from tensorflow.python.keras.layers import GlobalMaxPool2D as GlobalMaxPooling2D
from tensorflow.python.keras.layers import GlobalMaxPool3D
from tensorflow.python.keras.layers import GlobalMaxPool3D as GlobalMaxPooling3D
from tensorflow.python.keras.layers import LSTM
from tensorflow.python.keras.layers import LSTMCell
from tensorflow.python.keras.layers import Lambda
from tensorflow.python.keras.layers import LayerNormalization
from tensorflow.python.keras.layers import LeakyReLU
from tensorflow.python.keras.layers import LocallyConnected1D
from tensorflow.python.keras.layers import LocallyConnected2D
from tensorflow.python.keras.layers import Masking
from tensorflow.python.keras.layers import MaxPool1D
from tensorflow.python.keras.layers import MaxPool1D as MaxPooling1D
from tensorflow.python.keras.layers import MaxPool2D
from tensorflow.python.keras.layers import MaxPool2D as MaxPooling2D
from tensorflow.python.keras.layers import MaxPool3D
from tensorflow.python.keras.layers import MaxPool3D as MaxPooling3D
from tensorflow.python.keras.layers import Maximum
from tensorflow.python.keras.layers import Minimum
from tensorflow.python.keras.layers import Multiply
from tensorflow.python.keras.layers import PReLU
from tensorflow.python.keras.layers import Permute
from tensorflow.python.keras.layers import RNN
from tensorflow.python.keras.layers import ReLU
from tensorflow.python.keras.layers import RepeatVector
from tensorflow.python.keras.layers import Reshape
from tensorflow.python.keras.layers import SeparableConv1D
from tensorflow.python.keras.layers import SeparableConv1D as SeparableConvolution1D
from tensorflow.python.keras.layers import SeparableConv2D
from tensorflow.python.keras.layers import SeparableConv2D as SeparableConvolution2D
from tensorflow.python.keras.layers import SimpleRNN
from tensorflow.python.keras.layers import SimpleRNNCell
from tensorflow.python.keras.layers import Softmax
from tensorflow.python.keras.layers import SpatialDropout1D
from tensorflow.python.keras.layers import SpatialDropout2D
from tensorflow.python.keras.layers import SpatialDropout3D
from tensorflow.python.keras.layers import StackedRNNCells
from tensorflow.python.keras.layers import Subtract
from tensorflow.python.keras.layers import ThresholdedReLU
from tensorflow.python.keras.layers import TimeDistributed
from tensorflow.python.keras.layers import UpSampling1D
from tensorflow.python.keras.layers import UpSampling2D
from tensorflow.python.keras.layers import UpSampling3D
from tensorflow.python.keras.layers import Wrapper
from tensorflow.python.keras.layers import ZeroPadding1D
from tensorflow.python.keras.layers import ZeroPadding2D
from tensorflow.python.keras.layers import ZeroPadding3D
from tensorflow.python.keras.layers import add
from tensorflow.python.keras.layers import average
from tensorflow.python.keras.layers import concatenate
from tensorflow.python.keras.layers import deserialize
from tensorflow.python.keras.layers import dot
from tensorflow.python.keras.layers import maximum
from tensorflow.python.keras.layers import minimum
from tensorflow.python.keras.layers import multiply
from tensorflow.python.keras.layers import serialize
from tensorflow.python.keras.layers import subtract

del _print_function

import sys as _sys
from tensorflow.python.util import deprecation_wrapper as _deprecation_wrapper

if not isinstance(_sys.modules[__name__], _deprecation_wrapper.DeprecationWrapper):
  _sys.modules[__name__] = _deprecation_wrapper.DeprecationWrapper(
      _sys.modules[__name__], "keras.layers")
