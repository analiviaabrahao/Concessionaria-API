import logging
from sqlite3 import IntegrityError, OperationalError

from flask_restful import abort
from src.model.Cliente import Cliente
from src.model.ContaBancaria import ContaBancaria
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from src.model.Base import db

def add_cliente(id: int, nome: str, cpf: str, cnh: str, email: str, telefone: str) -> Cliente:
    """
    Insert a Cliente in the database.
    """
    cliente = Cliente (id=id, nome=nome, cpf =cpf, cnh =cnh, email=email, telefone= telefone)

    # INSERT
    db.session.add(cliente)

    db.session.commit()

    return cliente

def get_clientes() -> list[Cliente]:
    """
    Get all Departamentos stored in the database.

    Returns:
        departamentos (list[Departamento]) -- contains all departamentos registered.
    """
    veiculos = db.session.query(Cliente).all()
    return veiculos

def get_cliente(id: int) -> Cliente:
    """
    Get departamento by id stored in the database.

    Returns:
        departamento (Departamento) -- contains one departamento registered.
    """
    cliente = db.session.query(Cliente).get(id)
    return cliente

def delete_cliente(id: int):
    """
    Delete cliente by id stored in the database.

    """
    try:
        # Obtenha o cliente
        cliente = db.session.query(Cliente).get(id)
        if not cliente:
            abort(404, message="Cliente não encontrado")

        # Delete as contas bancárias associadas ao cliente usando .has()
        db.session.query(ContaBancaria).filter(ContaBancaria.cliente.has(id=id)).delete(synchronize_session=False)
        
        # Depois, delete o cliente
        db.session.delete(cliente)
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

def update_cliente(id: int, nome: str, cpf: str, cnh: str, email: str, telefone: str) -> Cliente:
    """
    Insert a Funcionario in the database.
    """
    cliente = db.session.query(Cliente).get(id)
    
    cliente.nome=nome
    cliente.cpf=cpf
    cliente.cnh=cnh
    cliente.email=email
    cliente.telefone=telefone
   

    db.session.commit()

    return cliente