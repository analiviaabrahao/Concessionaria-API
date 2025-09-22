from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .Base import Base



class Veiculo(Base):
    __tablename__ = "veiculo"

    # Columns
    id = Column(
        "id",
        Integer,
        primary_key=True,
    )
    tipo = Column("tipo", String(150), nullable=False)
    placa = Column("placa", String(7), nullable=False)
    marca = Column("marca", String(45), nullable=False)
    modelo = Column("modelo", String(45), nullable=False)
    pendencia = Column("pendencia", String(45), nullable=True)
    renavam = Column("renavam", Integer, nullable=False)
    km = Column("km", Float, nullable=False)




    #negociacoes = relationship("Negociacao", back_populates ="veicul")

    #relationships

    #relatioships
    negociacoes = relationship("Negociacao", back_populates="veiculo")

