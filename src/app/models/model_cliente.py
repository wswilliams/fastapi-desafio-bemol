from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database.db import Base


# SQLAlchemy Model


class Cliente(Base):

    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    cpf = Column(String(20))
    cep = Column(String(20))
    endereco = Column(String)
    telefone = Column(String)
    created_date = Column(DateTime, default=func.now(), nullable=False)

    def __init__(self, nome, cpf, cep, endereco, telefone):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep
        self.endereco = endereco
        self.telefone = telefone


# Pydantic Model

class ClienteSchema(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50)
    cpf: str = Field(..., min_length=3, max_length=15)
    cep: str = Field(..., min_length=3, max_length=50)
    endereco: str = Field(..., min_length=3, max_length=5100)
    telefone: str = Field(..., min_length=3, max_length=20)


class ClienteDB(ClienteSchema):
    id: int

    class Config:
        orm_mode = True
