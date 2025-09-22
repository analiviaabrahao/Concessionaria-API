from src.model.ContaBancaria import ContaBancaria
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from src.model.Base import db

def add_contabancaria(id: int, agencia: str, banco: str, status: str, id_cliente : int) -> ContaBancaria:
    """
    Insert a contabancaria in the database.
    """
    contabancaria = ContaBancaria (id = id, agencia = agencia, banco = banco ,status = status, id_cliente = id_cliente)

    # INSERT
    db.session.add(contabancaria)

    db.session.commit()

    return contabancaria

def get_contasbancarias() -> list[ContaBancaria]:
    """
    Get all Departamentos stored in the database.

    Returns:
        departamentos (list[Departamento]) -- contains all departamentos registered.
    """
    contabancaria = db.session.query(ContaBancaria).all()
    return contabancaria

def get_contabancaria(id: int) -> ContaBancaria:
    """
    Get departamento by id stored in the database.

    Returns:
        departamento (Departamento) -- contains one departamento registered.
    """
    contabancaria = db.session.query(ContaBancaria).get(id)
    return contabancaria