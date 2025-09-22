from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Numeric
from datetime import date
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.orm import relationship
from .Base import Base
from .Cliente import Cliente
from .Veiculo import Veiculo



class Negociacao(Base):
    __tablename__ = "negociacao"

    # Columns
    id = Column(
        "id",
        Integer,
        primary_key=True,
    )
    valor_fipe = Column("valor_fipe",Integer, nullable=False)
    valor_compra = Column("valor_compra",Integer, nullable=False)
    valor_venda = Column("valor_venda", Integer, nullable=False)
    status = Column("status", String(45), nullable=True)
    data_contrato = Column("data_contrato", Date, nullable=False)
   
    
    
    
   
    #negociacao_veiculo_fk = ForeignKey("veiculo.id", ondelete= "SET NULL")
    #negociacao_cliente_fk = ForeignKey("cliente.id", ondelete="SET NULL")
    #id_cliente = Column("id_cliente", negociacao_cliente_fk, nullable=False)
    #id_veiculo = Column("id_veiculo", negociacao_veiculo_fk, nullable=False)

    id_veiculo = Column(Integer, ForeignKey("veiculo.id", ondelete="SET NULL"), nullable=False)
    id_cliente = Column(Integer, ForeignKey("cliente.id", ondelete="SET NULL"), nullable=False)


  #Relationships
    cliente = relationship("Cliente", back_populates= "negociacoes")
    veiculo = relationship("Veiculo", back_populates= "negociacoes")



    