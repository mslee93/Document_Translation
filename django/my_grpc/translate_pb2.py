# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: translate.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='translate.proto',
  package='Translate',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0ftranslate.proto\x12\tTranslate\"y\n\x10translateRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x11\n\tfile_data\x18\x03 \x01(\x0c\x12\x10\n\x08src_lang\x18\x04 \x01(\t\x12\x10\n\x08tgt_lang\x18\x05 \x01(\t\x12\x0b\n\x03\x65ng\x18\x06 \x01(\t\"&\n\x11translateResponse\x12\x11\n\tfile_data\x18\x01 \x01(\x0c\x32U\n\tTranslate\x12H\n\ttranslate\x12\x1b.Translate.translateRequest\x1a\x1c.Translate.translateResponse\"\x00\x62\x06proto3'
)




_TRANSLATEREQUEST = _descriptor.Descriptor(
  name='translateRequest',
  full_name='Translate.translateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='Translate.translateRequest.job_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='Translate.translateRequest.file_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_data', full_name='Translate.translateRequest.file_data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_lang', full_name='Translate.translateRequest.src_lang', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tgt_lang', full_name='Translate.translateRequest.tgt_lang', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eng', full_name='Translate.translateRequest.eng', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=30,
  serialized_end=151,
)


_TRANSLATERESPONSE = _descriptor.Descriptor(
  name='translateResponse',
  full_name='Translate.translateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_data', full_name='Translate.translateResponse.file_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=153,
  serialized_end=191,
)

DESCRIPTOR.message_types_by_name['translateRequest'] = _TRANSLATEREQUEST
DESCRIPTOR.message_types_by_name['translateResponse'] = _TRANSLATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

translateRequest = _reflection.GeneratedProtocolMessageType('translateRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSLATEREQUEST,
  '__module__' : 'translate_pb2'
  # @@protoc_insertion_point(class_scope:Translate.translateRequest)
  })
_sym_db.RegisterMessage(translateRequest)

translateResponse = _reflection.GeneratedProtocolMessageType('translateResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSLATERESPONSE,
  '__module__' : 'translate_pb2'
  # @@protoc_insertion_point(class_scope:Translate.translateResponse)
  })
_sym_db.RegisterMessage(translateResponse)



_TRANSLATE = _descriptor.ServiceDescriptor(
  name='Translate',
  full_name='Translate.Translate',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=193,
  serialized_end=278,
  methods=[
  _descriptor.MethodDescriptor(
    name='translate',
    full_name='Translate.Translate.translate',
    index=0,
    containing_service=None,
    input_type=_TRANSLATEREQUEST,
    output_type=_TRANSLATERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSLATE)

DESCRIPTOR.services_by_name['Translate'] = _TRANSLATE

# @@protoc_insertion_point(module_scope)
