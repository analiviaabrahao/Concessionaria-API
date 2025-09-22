import re

from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.NegociacaoService import get_negociacao, add_negociacao, get_negociacoes


class NegociacaoResponseSchema(Schema):
    id = fields.Int()
    valor_fipe = fields.Int()
    valor_venda = fields.Int()
    valor_compra = fields.Int()
    status = fields.Str()
    id_veiculo = fields.Int()
    id_cliente = fields.Int()
    data_contrato = fields.Date()

    


class NegociacaoRequestSchema(Schema):
    id = fields.Int()
    status = fields.Str()
    valor_fipe = fields.Int()
    valor_venda = fields.Int()
    valor_compra = fields.Int()
    id_veiculo = fields.Int()
    id_cliente = fields.Int()
    data_contrato = fields.Date()



    
   # @validates("status")
    #def validate_name(self, value):
     #   if not re.match(pattern=r"^[a-zA-Z0-9_]+$", string=value):
      #      raise ValidationError(
       #         "Value must contain only alphanumeric and underscore characters."
        #    )
        
class NegociacaoItem(MethodResource, Resource):
    @marshal_with(NegociacaoResponseSchema)
    def get(self, negociacao_id):
        try:
            negociacao = get_negociacao(negociacao_id)
            if not negociacao:
                abort(404, message="Resource not found")
            return negociacao, 200
        except OperationalError:
            abort(500, message="Internal Server Error")



    @use_kwargs(NegociacaoRequestSchema, location=("json"))
    @marshal_with(NegociacaoResponseSchema)
    def put(self, negociacao_id, **kwargs):
        pass
        #try:
            #funcionario = update_funcionario(**kwargs, id=funcionario_id)
            #return funcionario, 200
        #except (OperationalError, IntegrityError):
         #   abort(500, message="Internal Server Error")


class NegociacaoList(MethodResource, Resource):
    @marshal_with(NegociacaoResponseSchema(many=True))
    def get(self):
        try:
            return  get_negociacoes(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(NegociacaoRequestSchema, location=("json"))
    @marshal_with(NegociacaoResponseSchema)
    def post(self, **kwargs):
        try:
           negociacao =  add_negociacao(**kwargs)
           return negociacao, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))