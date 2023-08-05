# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/contrib/session_bundle/manifest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/contrib/session_bundle/manifest.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0tensorflow/contrib/session_bundle/manifest.proto\x12\x12tensorflow.serving\"\xec\x01\n\nSignatures\x12\x38\n\x11\x64\x65\x66\x61ult_signature\x18\x01 \x01(\x0b\x32\x1d.tensorflow.serving.Signature\x12M\n\x10named_signatures\x18\x02 \x03(\x0b\x32\x33.tensorflow.serving.Signatures.NamedSignaturesEntry\x1aU\n\x14NamedSignaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.tensorflow.serving.Signature:\x02\x38\x01\"$\n\rTensorBinding\x12\x13\n\x0btensor_name\x18\x01 \x01(\t\"X\n\tAssetFile\x12\x39\n\x0etensor_binding\x18\x01 \x01(\x0b\x32!.tensorflow.serving.TensorBinding\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\"\xf0\x01\n\tSignature\x12G\n\x14regression_signature\x18\x01 \x01(\x0b\x32\'.tensorflow.serving.RegressionSignatureH\x00\x12O\n\x18\x63lassification_signature\x18\x02 \x01(\x0b\x32+.tensorflow.serving.ClassificationSignatureH\x00\x12\x41\n\x11generic_signature\x18\x03 \x01(\x0b\x32$.tensorflow.serving.GenericSignatureH\x00\x42\x06\n\x04type\"z\n\x13RegressionSignature\x12\x30\n\x05input\x18\x01 \x01(\x0b\x32!.tensorflow.serving.TensorBinding\x12\x31\n\x06output\x18\x02 \x01(\x0b\x32!.tensorflow.serving.TensorBinding\"\xb2\x01\n\x17\x43lassificationSignature\x12\x30\n\x05input\x18\x01 \x01(\x0b\x32!.tensorflow.serving.TensorBinding\x12\x32\n\x07\x63lasses\x18\x02 \x01(\x0b\x32!.tensorflow.serving.TensorBinding\x12\x31\n\x06scores\x18\x03 \x01(\x0b\x32!.tensorflow.serving.TensorBinding\"\x9d\x01\n\x10GenericSignature\x12:\n\x03map\x18\x01 \x03(\x0b\x32-.tensorflow.serving.GenericSignature.MapEntry\x1aM\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.tensorflow.serving.TensorBinding:\x02\x38\x01\x62\x06proto3')
)




_SIGNATURES_NAMEDSIGNATURESENTRY = _descriptor.Descriptor(
  name='NamedSignaturesEntry',
  full_name='tensorflow.serving.Signatures.NamedSignaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.serving.Signatures.NamedSignaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.serving.Signatures.NamedSignaturesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=309,
)

_SIGNATURES = _descriptor.Descriptor(
  name='Signatures',
  full_name='tensorflow.serving.Signatures',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='default_signature', full_name='tensorflow.serving.Signatures.default_signature', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='named_signatures', full_name='tensorflow.serving.Signatures.named_signatures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SIGNATURES_NAMEDSIGNATURESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=309,
)


_TENSORBINDING = _descriptor.Descriptor(
  name='TensorBinding',
  full_name='tensorflow.serving.TensorBinding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_name', full_name='tensorflow.serving.TensorBinding.tensor_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=311,
  serialized_end=347,
)


_ASSETFILE = _descriptor.Descriptor(
  name='AssetFile',
  full_name='tensorflow.serving.AssetFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_binding', full_name='tensorflow.serving.AssetFile.tensor_binding', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='tensorflow.serving.AssetFile.filename', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=349,
  serialized_end=437,
)


_SIGNATURE = _descriptor.Descriptor(
  name='Signature',
  full_name='tensorflow.serving.Signature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='regression_signature', full_name='tensorflow.serving.Signature.regression_signature', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classification_signature', full_name='tensorflow.serving.Signature.classification_signature', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generic_signature', full_name='tensorflow.serving.Signature.generic_signature', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
      name='type', full_name='tensorflow.serving.Signature.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=440,
  serialized_end=680,
)


_REGRESSIONSIGNATURE = _descriptor.Descriptor(
  name='RegressionSignature',
  full_name='tensorflow.serving.RegressionSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='tensorflow.serving.RegressionSignature.input', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='tensorflow.serving.RegressionSignature.output', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=682,
  serialized_end=804,
)


_CLASSIFICATIONSIGNATURE = _descriptor.Descriptor(
  name='ClassificationSignature',
  full_name='tensorflow.serving.ClassificationSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='tensorflow.serving.ClassificationSignature.input', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classes', full_name='tensorflow.serving.ClassificationSignature.classes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scores', full_name='tensorflow.serving.ClassificationSignature.scores', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=807,
  serialized_end=985,
)


_GENERICSIGNATURE_MAPENTRY = _descriptor.Descriptor(
  name='MapEntry',
  full_name='tensorflow.serving.GenericSignature.MapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.serving.GenericSignature.MapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.serving.GenericSignature.MapEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1068,
  serialized_end=1145,
)

_GENERICSIGNATURE = _descriptor.Descriptor(
  name='GenericSignature',
  full_name='tensorflow.serving.GenericSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='map', full_name='tensorflow.serving.GenericSignature.map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GENERICSIGNATURE_MAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=988,
  serialized_end=1145,
)

_SIGNATURES_NAMEDSIGNATURESENTRY.fields_by_name['value'].message_type = _SIGNATURE
_SIGNATURES_NAMEDSIGNATURESENTRY.containing_type = _SIGNATURES
_SIGNATURES.fields_by_name['default_signature'].message_type = _SIGNATURE
_SIGNATURES.fields_by_name['named_signatures'].message_type = _SIGNATURES_NAMEDSIGNATURESENTRY
_ASSETFILE.fields_by_name['tensor_binding'].message_type = _TENSORBINDING
_SIGNATURE.fields_by_name['regression_signature'].message_type = _REGRESSIONSIGNATURE
_SIGNATURE.fields_by_name['classification_signature'].message_type = _CLASSIFICATIONSIGNATURE
_SIGNATURE.fields_by_name['generic_signature'].message_type = _GENERICSIGNATURE
_SIGNATURE.oneofs_by_name['type'].fields.append(
  _SIGNATURE.fields_by_name['regression_signature'])
_SIGNATURE.fields_by_name['regression_signature'].containing_oneof = _SIGNATURE.oneofs_by_name['type']
_SIGNATURE.oneofs_by_name['type'].fields.append(
  _SIGNATURE.fields_by_name['classification_signature'])
_SIGNATURE.fields_by_name['classification_signature'].containing_oneof = _SIGNATURE.oneofs_by_name['type']
_SIGNATURE.oneofs_by_name['type'].fields.append(
  _SIGNATURE.fields_by_name['generic_signature'])
_SIGNATURE.fields_by_name['generic_signature'].containing_oneof = _SIGNATURE.oneofs_by_name['type']
_REGRESSIONSIGNATURE.fields_by_name['input'].message_type = _TENSORBINDING
_REGRESSIONSIGNATURE.fields_by_name['output'].message_type = _TENSORBINDING
_CLASSIFICATIONSIGNATURE.fields_by_name['input'].message_type = _TENSORBINDING
_CLASSIFICATIONSIGNATURE.fields_by_name['classes'].message_type = _TENSORBINDING
_CLASSIFICATIONSIGNATURE.fields_by_name['scores'].message_type = _TENSORBINDING
_GENERICSIGNATURE_MAPENTRY.fields_by_name['value'].message_type = _TENSORBINDING
_GENERICSIGNATURE_MAPENTRY.containing_type = _GENERICSIGNATURE
_GENERICSIGNATURE.fields_by_name['map'].message_type = _GENERICSIGNATURE_MAPENTRY
DESCRIPTOR.message_types_by_name['Signatures'] = _SIGNATURES
DESCRIPTOR.message_types_by_name['TensorBinding'] = _TENSORBINDING
DESCRIPTOR.message_types_by_name['AssetFile'] = _ASSETFILE
DESCRIPTOR.message_types_by_name['Signature'] = _SIGNATURE
DESCRIPTOR.message_types_by_name['RegressionSignature'] = _REGRESSIONSIGNATURE
DESCRIPTOR.message_types_by_name['ClassificationSignature'] = _CLASSIFICATIONSIGNATURE
DESCRIPTOR.message_types_by_name['GenericSignature'] = _GENERICSIGNATURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Signatures = _reflection.GeneratedProtocolMessageType('Signatures', (_message.Message,), dict(

  NamedSignaturesEntry = _reflection.GeneratedProtocolMessageType('NamedSignaturesEntry', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATURES_NAMEDSIGNATURESENTRY,
    __module__ = 'tensorflow.contrib.session_bundle.manifest_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.serving.Signatures.NamedSignaturesEntry)
    ))
  ,
  DESCRIPTOR = _SIGNATURES,
  __module__ = 'tensorflow.contrib.session_bundle.manifest_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.Signatures)
  ))
_sym_db.RegisterMessage(Signatures)
_sym_db.RegisterMessage(Signatures.NamedSignaturesEntry)

TensorBinding = _reflection.GeneratedProtocolMessageType('TensorBinding', (_message.Message,), dict(
  DESCRIPTOR = _TENSORBINDING,
  __module__ = 'tensorflow.contrib.session_bundle.manifest_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.TensorBinding)
  ))
_sym_db.RegisterMessage(TensorBinding)

AssetFile = _reflection.GeneratedProtocolMessageType('AssetFile', (_message.Message,), dict(
  DESCRIPTOR = _ASSETFILE,
  __module__ = 'tensorflow.contrib.session_bundle.manifest_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.AssetFile)
  ))
_sym_db.RegisterMessage(AssetFile)

Signature = _reflection.GeneratedProtocolMessageType('Signature', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATURE,
  __module__ = 'tensorflow.contrib.session_bundle.manifest_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.Signature)
  ))
_sym_db.RegisterMessage(Signature)

RegressionSignature = _reflection.GeneratedProtocolMessageType('RegressionSignature', (_message.Message,), dict(
  DESCRIPTOR = _REGRESSIONSIGNATURE,
  __module__ = 'tensorflow.contrib.session_bundle.manifest_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.RegressionSignature)
  ))
_sym_db.RegisterMessage(RegressionSignature)

ClassificationSignature = _reflection.GeneratedProtocolMessageType('ClassificationSignature', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFICATIONSIGNATURE,
  __module__ = 'tensorflow.contrib.session_bundle.manifest_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.ClassificationSignature)
  ))
_sym_db.RegisterMessage(ClassificationSignature)

GenericSignature = _reflection.GeneratedProtocolMessageType('GenericSignature', (_message.Message,), dict(

  MapEntry = _reflection.GeneratedProtocolMessageType('MapEntry', (_message.Message,), dict(
    DESCRIPTOR = _GENERICSIGNATURE_MAPENTRY,
    __module__ = 'tensorflow.contrib.session_bundle.manifest_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.serving.GenericSignature.MapEntry)
    ))
  ,
  DESCRIPTOR = _GENERICSIGNATURE,
  __module__ = 'tensorflow.contrib.session_bundle.manifest_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.GenericSignature)
  ))
_sym_db.RegisterMessage(GenericSignature)
_sym_db.RegisterMessage(GenericSignature.MapEntry)


_SIGNATURES_NAMEDSIGNATURESENTRY._options = None
_GENERICSIGNATURE_MAPENTRY._options = None
# @@protoc_insertion_point(module_scope)
