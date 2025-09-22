import re

from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.ContaBancariaService import get_contasbancarias , addcontabancaria, get_contabancaria


class ContaBancariaResponseSchema(Schema):
    id = fields.Int()
    agencia = fields.Int()
    banco = fields.Str()
    status = fields.Str()
    id_cliente = fields.Int()
    


class ContaBancariaRequestSchema(Schema):
    id = fields.Int()
    agencia = fields.Int()
    banco = fields.Str()
    status = fields.Str()
    id_cliente = fields.Int()



    @validates("banco")
    def validate_banco(self, value):
        if not re.match(pattern=r"^[a-zA-Z0-9_]+$", string=value):
            raise ValidationError(
                "Value must contain only alphanumeric and underscore characters."
            )

        
class ContaBancariaItem(MethodResource, Resource):
    @marshal_with(ContaBancariaResponseSchema)
    def get(self, contabancaria_id):
        try:
            contabancaria = get_contabancaria(contabancaria_id)
            if not contabancaria:
                abort(404, message="Resource not found")
            return contabancaria, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    #def delete(self,contabancaria_id):
     #   try:
      #      deletecontabancaria(contabancaria_id)
       #     return "", 204
        #except UnmappedInstanceError:
         #   abort(404, message="Resource not found")
        #except (OperationalError, IntegrityError):
         #   abort(500, message="Internal Server Error")

    @use_kwargs(ContaBancariaRequestSchema, location=("form"))
    @marshal_with(ContaBancariaResponseSchema)
    def put(self, contabancaria_id, **kwargs):
        pass
        #try:
            #funcionario = update_funcionario(**kwargs, id=funcionario_id)
            #return funcionario, 200
        #except (OperationalError, IntegrityError):
         #   abort(500, message="Internal Server Error")


class ContaBancariaList(MethodResource, Resource):
    @marshal_with(ContaBancariaResponseSchema(many=True))
    def get(self):
        try:
            return  get_contasbancarias (), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(ContaBancariaRequestSchema, location=("form"))
    @marshal_with(ContaBancariaResponseSchema)
    def post(self, **kwargs):
        try:
            contabancaria = addcontabancaria(**kwargs)
            return contabancaria, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
