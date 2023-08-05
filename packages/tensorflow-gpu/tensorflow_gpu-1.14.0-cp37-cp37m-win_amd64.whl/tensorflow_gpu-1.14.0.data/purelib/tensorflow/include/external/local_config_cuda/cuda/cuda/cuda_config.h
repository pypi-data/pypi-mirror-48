/* Copyright 2015 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#ifndef CUDA_CUDA_CONFIG_H_
#define CUDA_CUDA_CONFIG_H_

#define TF_CUDA_CAPABILITIES CudaVersion("3.5"), CudaVersion("3.7"), CudaVersion("5.2"), CudaVersion("6.0"), CudaVersion("6.1"), CudaVersion("7.0")

#define TF_CUDA_VERSION "64_100"
#define TF_CUDA_LIB_VERSION "64_100"
#define TF_CUDNN_VERSION "64_7"

#define TF_CUDA_TOOLKIT_PATH "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v10.0"

#endif  // CUDA_CUDA_CONFIG_H_
