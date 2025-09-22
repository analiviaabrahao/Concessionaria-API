import re

from marshmallow import ValidationError
from src.model.Veiculo import Veiculo
from src.model.Base import db
from src.repositories.VeiculoRepository import delete_veiculo, get_veiculo, add_veiculo, get_veiculos, delete_veiculo, update_veiculo

def addVeiculo(id: int, tipo: str, placa: str, marca: str, modelo: str, km: float, pendencia: str, renavam: int) -> Veiculo:
    if(id is None or id == '' or tipo is None or tipo == '' or placa is None or placa == '' or marca is None or marca == '' or modelo is None or modelo == '' or km is None or km == '' or pendencia is None or pendencia == '' or renavam is None or renavam == ''):
        raise Exception
   
    #valida a quilometragem
    if(km < 0):
        raise Exception("A quilometragem não pode ser nagativa!")
    

    if not re.match(r"^[a-zA-Z0-9_]{7}$", placa):
        raise ValidationError("Placa nao permmitida")



    return add_veiculo(id, tipo, placa, marca, modelo, km, pendencia, renavam)

def getVeiculos() -> list[Veiculo]:
    return get_veiculos()

def getVeiculo(id: int) -> Veiculo:
    return get_veiculo(id)

def deleteVeiculo(id: int):
    delete_veiculo(id) 

def updateVeiculo(id: int, tipo: str, placa: str, marca: str, modelo: str, km: float, pendencia: str, renavam: int) -> Veiculo:
    return update_veiculo (id=id, tipo=tipo, placa=placa, marca=marca,modelo=modelo, km=km, pendencia=pendencia, renavam=renavam )