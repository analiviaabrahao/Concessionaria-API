import logging
from sqlite3 import IntegrityError, OperationalError
from flask_restful import abort
from src.model.Veiculo import Veiculo
from src.model.Negociacao import Negociacao
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from src.model.Base import db

def add_veiculo(id: int, tipo: str, placa: str, marca: str, modelo: str, km: float, pendencia: str, renavam: int) -> Veiculo:
    """
    Insert a veiculo in the database.
    """
    veiculo = Veiculo(id=id, tipo=tipo, placa=placa, marca= marca, modelo = modelo, km = km, pendencia =pendencia, renavam= renavam)
    
    # INSERT
    db.session.add(veiculo)

    db.session.commit()

    return veiculo

def get_veiculos() -> list[Veiculo]:
    """
    Get all veiculos stored in the database.

    Returns:
        veiculos (Veiculo) -- contains all veiculos registered.
    """
    veiculos = db.session.query(Veiculo).all()
    return veiculos

def get_veiculo(id: int) -> Veiculo:
    """
    Get funcionario by id stored in the database.

    Returns:
        funcionario (Funcionario) -- contains one funcionario registered.
    """
    veiculo = db.session.query(Veiculo).get(id)
    return veiculo

def delete_veiculo(id: int):
    """
    Delete cliente by id stored in the database.

    """
    try:
        # Obtenha o cliente
        veiculo = db.session.query(Veiculo).get(id)
        if not veiculo:
            abort(404, message="Cliente não encontrado")

        # Delete as contas bancárias associadas ao cliente usando .has()
        db.session.query(Negociacao).filter(Negociacao.veiculo.has(id=id)).delete(synchronize_session=False)
        
        # Depois, delete o cliente
        db.session.delete(veiculo)
        db.session.commit()

    except OperationalError as e:
        db.session.rollback()
        logging.error(f"OperationalError: {str(e)}")
        abort(500, message=f"Erro operacional: {str(e)}")
    
    except IntegrityError as e:
        db.session.rollback()
        logging.error(f"IntegrityError: {str(e)}")
        abort(500, message=f"Erro de integridade: {str(e)}")
    
    except Exception as e:
        db.session.rollback()
        logging.error(f"Exception: {str(e)}")
        abort(500, message=f"Erro desconhecido: {str(e)}")


def update_veiculo(id: int, tipo: str, placa: str, marca: str, modelo: str, km: float, pendencia: str, renavam: int) -> Veiculo:
    """
    Insert a Funcionario in the database.
    """
    veiculo = db.session.query(Veiculo).get(id)
    
    veiculo.tipo = tipo
    veiculo.placa = placa
    veiculo.marca = marca
    veiculo.modelo = modelo
    veiculo.km = km
    veiculo.pendencia = pendencia
    veiculo.renavam = renavam


    db.session.commit()

    return veiculo