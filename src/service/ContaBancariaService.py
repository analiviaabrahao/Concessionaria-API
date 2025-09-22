from src.model.ContaBancaria import ContaBancaria
from src.repositories.ContaBancariaRepository import get_contabancaria, add_contabancaria, get_contasbancarias




def addcontabancaria(id: int, agencia: str, banco: str, status: str,  id_cliente = None) -> ContaBancaria:
 if(id is None or id == '' or agencia is None or agencia == '' or  banco is None or banco == '' or status is None or status == '' ):        
    raise Exception
 return add_contabancaria(id,agencia, banco, status, id_cliente)

def getcontasbancarias() -> list[ContaBancaria]:
    return get_contasbancarias()

def getcontabancaria(id: int) -> ContaBancaria:
    return get_contabancaria(id)