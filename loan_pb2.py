# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loan.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='loan.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nloan.proto\"_\n\tloan_data\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x15\n\rinterest_rate\x18\x02 \x01(\x01\x12\x17\n\x0frepayment_terms\x18\x03 \x01(\x05\x12\x13\n\x0bloan_amount\x18\x04 \x01(\x01\"\"\n\x11installement_data\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"5\n\x15installement_response\x12\x1c\n\x14installement_message\x18\x01 \x01(\t\"9\n\x0erepayment_data\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x18\n\x10repayment_amount\x18\x02 \x01(\x01\"\x07\n\x05\x65mpty2\x93\x01\n\x04Loan\x12!\n\tsave_loan\x12\n.loan_data\x1a\x06.empty\"\x00\x12@\n\x10show_installment\x12\x12.installement_data\x1a\x16.installement_response\"\x00\x12&\n\trepayment\x12\x0f.repayment_data\x1a\x06.empty\"\x00\x62\x06proto3'
)




_LOAN_DATA = _descriptor.Descriptor(
  name='loan_data',
  full_name='loan_data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='loan_data.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interest_rate', full_name='loan_data.interest_rate', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repayment_terms', full_name='loan_data.repayment_terms', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loan_amount', full_name='loan_data.loan_amount', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=14,
  serialized_end=109,
)


_INSTALLEMENT_DATA = _descriptor.Descriptor(
  name='installement_data',
  full_name='installement_data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='installement_data.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=111,
  serialized_end=145,
)


_INSTALLEMENT_RESPONSE = _descriptor.Descriptor(
  name='installement_response',
  full_name='installement_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='installement_message', full_name='installement_response.installement_message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=147,
  serialized_end=200,
)


_REPAYMENT_DATA = _descriptor.Descriptor(
  name='repayment_data',
  full_name='repayment_data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='repayment_data.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repayment_amount', full_name='repayment_data.repayment_amount', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=202,
  serialized_end=259,
)


_EMPTY = _descriptor.Descriptor(
  name='empty',
  full_name='empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=261,
  serialized_end=268,
)

DESCRIPTOR.message_types_by_name['loan_data'] = _LOAN_DATA
DESCRIPTOR.message_types_by_name['installement_data'] = _INSTALLEMENT_DATA
DESCRIPTOR.message_types_by_name['installement_response'] = _INSTALLEMENT_RESPONSE
DESCRIPTOR.message_types_by_name['repayment_data'] = _REPAYMENT_DATA
DESCRIPTOR.message_types_by_name['empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

loan_data = _reflection.GeneratedProtocolMessageType('loan_data', (_message.Message,), {
  'DESCRIPTOR' : _LOAN_DATA,
  '__module__' : 'loan_pb2'
  # @@protoc_insertion_point(class_scope:loan_data)
  })
_sym_db.RegisterMessage(loan_data)

installement_data = _reflection.GeneratedProtocolMessageType('installement_data', (_message.Message,), {
  'DESCRIPTOR' : _INSTALLEMENT_DATA,
  '__module__' : 'loan_pb2'
  # @@protoc_insertion_point(class_scope:installement_data)
  })
_sym_db.RegisterMessage(installement_data)

installement_response = _reflection.GeneratedProtocolMessageType('installement_response', (_message.Message,), {
  'DESCRIPTOR' : _INSTALLEMENT_RESPONSE,
  '__module__' : 'loan_pb2'
  # @@protoc_insertion_point(class_scope:installement_response)
  })
_sym_db.RegisterMessage(installement_response)

repayment_data = _reflection.GeneratedProtocolMessageType('repayment_data', (_message.Message,), {
  'DESCRIPTOR' : _REPAYMENT_DATA,
  '__module__' : 'loan_pb2'
  # @@protoc_insertion_point(class_scope:repayment_data)
  })
_sym_db.RegisterMessage(repayment_data)

empty = _reflection.GeneratedProtocolMessageType('empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'loan_pb2'
  # @@protoc_insertion_point(class_scope:empty)
  })
_sym_db.RegisterMessage(empty)



_LOAN = _descriptor.ServiceDescriptor(
  name='Loan',
  full_name='Loan',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=271,
  serialized_end=418,
  methods=[
  _descriptor.MethodDescriptor(
    name='save_loan',
    full_name='Loan.save_loan',
    index=0,
    containing_service=None,
    input_type=_LOAN_DATA,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='show_installment',
    full_name='Loan.show_installment',
    index=1,
    containing_service=None,
    input_type=_INSTALLEMENT_DATA,
    output_type=_INSTALLEMENT_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='repayment',
    full_name='Loan.repayment',
    index=2,
    containing_service=None,
    input_type=_REPAYMENT_DATA,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOAN)

DESCRIPTOR.services_by_name['Loan'] = _LOAN

# @@protoc_insertion_point(module_scope)
