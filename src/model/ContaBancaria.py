from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base


class ContaBancaria(Base):
    __tablename__ = "contabancaria"

    # Columns
    id = Column(
        "id",
        Integer,
        primary_key=True,
    )
    agencia = Column("agencia", String(45), nullable=False)
    banco = Column("banco", String(45), nullable=False)
    status= Column("status", String(45), nullable=True)
    
    
     

    #contabancaria_cliente_fk = ForeignKey("cliente.id", ondelete="SET NULL")
    #id_cliente = Column("id_cliente", contabancaria_cliente_fk, nullable=False)
    
    
    id_cliente = Column(Integer, ForeignKey("cliente.id", ondelete="SET NULL"), nullable=False)

    #relatioships
    cliente = relationship("Cliente", back_populates= "cliente_contabancaria")
