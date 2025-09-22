from datetime import date
from typing import Any
from datetime import date
import logging
from sqlite3 import IntegrityError, OperationalError
from typing import Any
from flask_restful import abort
from src.model.Cliente import Cliente
from src.model.ContaBancaria import ContaBancaria
#from Concessionaria.src.model import Cliente, ContaBancaria
from src.model.Negociacao import Negociacao
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from src.model.Base import db


def add_negociacao(id: int,valor_fipe: int, valor_compra : int, valor_venda: int, id_veiculo: int, id_cliente: int, status: str, data_contrato: date) -> Negociacao:
    """
    Insert a negociacao in the database.
    """

    negociacao = Negociacao (id=id, valor_fipe= valor_fipe, valor_compra=valor_compra, valor_venda=valor_venda, id_veiculo=id_veiculo, id_cliente=id_cliente, status=status, data_contrato = data_contrato)

    # INSERT
    db.session.add(negociacao)

    db.session.commit()

    return negociacao

def get_negociacoes() -> list[Negociacao]:
    """
    Get all Departamentos stored in the database.

    Returns:
        departamentos (list[Departamento]) -- contains all departamentos registered.
    """
    veiculos = db.session.query(Negociacao).all()
    return veiculos
def delete_negociacao(id: int):
    """
    Delete cliente by id stored in the database.

    """
    try:
        # Obtenha o cliente
        negociacao = db.session.query(Negociacao).get(id)
        if not negociacao:
            abort(404, message=" não encontrado")
        
        # Depois, delete 
        db.session.delete(negociacao)
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
        
        


    
def get_negociacao(id: int) -> Negociacao:
    """
    Get negociacao by id stored in the database.

    Returns:
        negociacao (Departamento) -- contains one departamento registered.
    """
    negociacao= db.session.query(Negociacao).get(id)
    return negociacao