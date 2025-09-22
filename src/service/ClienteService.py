from src.model.Cliente import Cliente
from src.repositories.ClienteRepository import get_cliente, add_cliente, get_clientes,  delete_cliente, update_cliente

def addcliente(id: int, nome: str, cpf: str, cnh: str, email: str, telefone: str) -> Cliente:
    if(id is None or id == '' or nome is None or nome == '' or cpf is None or cpf == '' or cnh is None or cnh == '' or email is None or email == '' or telefone is None or telefone == ''):
        raise Exception

    return add_cliente(id, nome, cpf, cnh, email, telefone)

def getclientes() -> list[Cliente]:
    return get_clientes()

def getcliente(id: int) -> Cliente:
    return get_cliente(id)

def deletecliente(id: int):
    delete_cliente(id)

def updateCliente(id: int, nome: str, cpf: str, cnh: str, email: str, telefone: str) -> Cliente:
    return update_cliente(id= id, nome=nome, cpf=cpf, cnh=cnh, email=email, telefone=telefone)