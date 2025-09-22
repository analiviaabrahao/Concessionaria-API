# 🚗 API Concessionária

API desenvolvida em **Python + Flask + SQLAlchemy** para gerenciar clientes, veículos, negociações e contas bancárias de uma concessionária.

--

Este Projeto se trata de uma iniciativa acadêmica feita exatamente para o meu desenvolvimento de conhecimento e desenvoltura com o uso das tecnologias citadas abaixo. Há muito a melhorar, porém acredito que com esse projeto foi possível aprender soluções e usos interessantes para aplicações futuras.

## 📌 Tecnologias Utilizadas
- Python 3.12
- Flask
- Flask-RESTful
- Flask-Apispec (documentação de rotas)
- SQLAlchemy (ORM)
- Marshmallow (validação de dados)
- PostgreSQL
- Psycopg2

---

## 🗄️ Modelagem do Banco de Dados

- **Cliente**
  - `id` (PK)
  - `nome`
  - `cpf`
  - `cnh`
  - `email`
  - `telefone`
  - Relacionamento: 1:N com `Negociacao` e `ContaBancaria`

- **Veiculo**
  - `id` (PK)
  - `tipo`
  - `placa`
  - `marca`
  - `modelo`
  - `pendencia`
  - `renavam`
  - `km`
  - Relacionamento: 1:N com `Negociacao`

- **Negociacao**
  - `id` (PK)
  - `id_cliente` (FK → Cliente)
  - `id_veiculo` (FK → Veiculo)
  - `valor_compra`
  - `valor_venda`
  - `valor_fipe` 
  - `status`
  - `data_contrato`
  
- **ContaBancaria**
  - `id` (PK)
  - `id_cliente` (FK → Cliente)
  - `banco`
  - `agencia`
  - `status`

## 📌 Endpoints Principais
👤 Clientes

POST /api/clientes → cria cliente

GET /api/clientes → lista clientes

GET /api/clientes/<id> → busca cliente por id

DELETE /api/clientes/<id> → remove cliente por id

🚗 Veículos

POST /api/veiculos → cria veículo

GET /api/veiculos → lista veículos

DELETE /api/veiculos/<id> → remove veiculo por id

📑 Negociações

POST /api/negociacoes → cria negociação

GET /api/negociacoes → lista negociações

🏦 Conta Bancária

POST /api/contas → cria conta bancária

GET /api/contas → lista contas



## ⚙️ Como Rodar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/analiviaabrahao/api-concessionaria.git
cd api-concessionaria
```


![Logo do projeto](https://github.com/analiviaabrahao/Concessionaria-API/blob/main/tela-principal.png)
![Logo do projeto](https://github.com/analiviaabrahao/Concessionaria-API/blob/main/Cap3.png)
![Logo do projeto](https://github.com/analiviaabrahao/Concessionaria-API/blob/main/Cap1.png)
![Logo do projeto](https://github.com/analiviaabrahao/Concessionaria-API/blob/main/Cap2.png)

