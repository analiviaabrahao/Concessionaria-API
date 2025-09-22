from src.controller.VeiculoController import VeiculoItem, VeiculoList
from src.controller.ClienteController import ClienteItem, ClienteList
from src.controller.ContaBancariaController import ContaBancariaItem, ContaBancariaList
from src.controller.NegociacaoController import NegociacaoItem, NegociacaoList
 
## Aula que vem
def initialize_endpoints(api):
    api.add_resource(VeiculoItem, "/veiculos/<int:veiculo_id>")
    api.add_resource(VeiculoList, "/veiculos")
    api.add_resource(ClienteList, "/clientes")
    api.add_resource(ClienteItem, "/clientes/<int:cliente_id>")
    api.add_resource(NegociacaoList, "/negociacoes")
    api.add_resource(ContaBancariaList, "/contas")
  
