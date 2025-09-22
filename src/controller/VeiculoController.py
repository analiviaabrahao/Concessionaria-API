import re

from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
#from Concessionaria.src.model import Veiculo
#from src.model.Base import db
from src.service.VeiculoService import getVeiculos, deleteVeiculo, addVeiculo, getVeiculo, updateVeiculo


class VeiculoResponseSchema(Schema):
    id = fields.Int()
    tipo = fields.Str()
    placa = fields.Str()
    marca = fields.Str()
    modelo = fields.Str()
    km = fields.Float()
    pendencia = fields.Str()
    renavam = fields.Int()
    


class VeiculoRequestSchema(Schema):
    id = fields.Int()
    tipo = fields.Str()
    placa = fields.Str()
    marca = fields.Str()
    modelo = fields.Str()
    km = fields.Float()
    pendencia = fields.Str()
    renavam = fields.Int()
    
    # @validates("placa")
    # def validate_placa(self, value):
    #     if not re.match(pattern=r"^[a-zA-Z0-9_]{7}$", string=value):
    #         raise ValidationError(
    #             "Value must contain only alphanumeric and underscore characters."
    #         )
        
 


    # @validates("marca")
    # @validates("modelo")
    # def validate_unique_vehicle(self, value, field):
    #     if field.name == "modelo":
    #         marca = self.get_value("marca")
    #         modelo = value
            
    #     # Verifica se já existe um veículo com o mesmo modelo, mas com uma marca diferente no banco
    #     veiculo = db.session.query(Veiculo).filter(Veiculo.modelo == modelo).first()

    #     if veiculo and veiculo.marca != marca:
    #         raise ValidationError(
    #             f"O modelo '{modelo}' já está associado à outra marca ('{veiculo.marca}'). Não é permitido o mesmo modelo com marcas diferentes."
    #         )

    #     return value
        
class VeiculoItem(MethodResource, Resource):
    @marshal_with(VeiculoResponseSchema)
    def get(self, veiculo_id):
        try:
            veiculo = getVeiculo(veiculo_id)
            if not veiculo:
                abort(404, message="Resource not found")
            return veiculo, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, veiculo_id):
        try:
            deleteVeiculo(veiculo_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @use_kwargs(VeiculoRequestSchema, location=("form"))
    @marshal_with(VeiculoResponseSchema)
    def put(self, veiculo_id, **kwargs):
        pass
        try:
            veiculo = updateVeiculo(**kwargs, id=veiculo_id)
            return veiculo, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

class VeiculoList(MethodResource, Resource):
    @marshal_with(VeiculoResponseSchema(many=True))
    def get(self):
        try:
            return getVeiculos(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(VeiculoRequestSchema, location=("form"))
    @marshal_with(VeiculoResponseSchema)
    def post(self, **kwargs):
        try:
            veiculo = addVeiculo(**kwargs)
            return veiculo, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
