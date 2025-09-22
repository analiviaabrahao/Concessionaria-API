import re

from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.ClienteService import getclientes,  addcliente, getcliente, delete_cliente, updateCliente


class ClienteResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    cpf = fields.Str()
    cnh = fields.Str()
    email = fields.Str()
    telefone = fields.Str()
    


class ClienteRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    cpf = fields.Str()
    cnh = fields.Str()
    email = fields.Str()
    telefone = fields.Str()
    
   # @validates("nome")
    #def validate_name(self, value):
     #   if not re.match(pattern=r"^[a-zA-Z0-9_]+$", string=value):
      #      raise ValidationError(
       #         "Value must contain only alphanumeric and underscore characters."
        #    )
        
class ClienteItem(MethodResource, Resource):
    @marshal_with(ClienteResponseSchema)
    def get(self, cliente_id):
        try:
            cliente = getcliente(cliente_id)
            if not cliente:
                abort(404, message="Resource not found")
            return cliente, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, cliente_id):
        try:
            delete_cliente(cliente_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Cliente nao encontrado")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @use_kwargs(ClienteRequestSchema, location=("form"))
    @marshal_with(ClienteResponseSchema)
    def put(self, cliente_id, **kwargs):
        pass
        try:
            cliente = updateCliente(**kwargs, id=cliente_id)
            return cliente, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


class ClienteList(MethodResource, Resource):
    @marshal_with(ClienteResponseSchema(many=True))
    def get(self):
        try:
            return getclientes(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(ClienteRequestSchema, location=("form"))
    @marshal_with(ClienteResponseSchema)
    def post(self, **kwargs):
        try:
            cliente = addcliente (**kwargs)
            return cliente, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
