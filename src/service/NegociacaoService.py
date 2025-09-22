from datetime import date
from src.model.Negociacao import Negociacao
from src.repositories.NegociacaoRepository import get_negociacao, add_negociacao, get_negociacoes



def addnegociacao(id: int,valor_fipe: int, valor_compra : int, valor_venda: int, id_veiculo: None, id_cliente: None, status: str, data_contrato: date) -> Negociacao:
   if(id is None or id == ''  or valor_fipe is None or valor_fipe == ''  or valor_compra is None or valor_compra == ''  or valor_venda is None or valor_venda == ''  or id_veiculo is None or id_veiculo == ''  or id_cliente is None or id_cliente == ''  or status is None or status == ''  or data_contrato is None or data_contrato == ''  ):
        raise Exception
     
   
   return add_negociacao(id, valor_compra, valor_fipe, valor_venda, id_cliente, id_veiculo, status, data_contrato)




def getnegociacoes() -> list[Negociacao]:
    return get_negociacoes()

def getnegociacao(id: int) -> Negociacao:
    return get_negociacao(id)

