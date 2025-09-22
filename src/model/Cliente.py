from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base



class Cliente(Base):
    __tablename__ = "cliente"

    # Columns
    id = Column(
        "id",
        Integer,
        primary_key=True,
    )
    nome = Column("nome", String(45), nullable=False)
    cpf = Column("cpf", String(14), nullable=False)
    cnh= Column("cnh", String(45), nullable=False)
    email= Column("email", String(45), nullable=False)
    telefone= Column("telefone", String(45), nullable=False)


    #cliente_negociacao = relationship("Negociacao", back_populates="cliente")
    cliente_contabancaria = relationship("ContaBancaria", back_populates="cliente")

    #relatioships
    #contabancaria = relationship("ContaBancaria", back_populates="cliente")
    negociacoes = relationship("Negociacao", back_populates="cliente")