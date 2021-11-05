from sqlalchemy import Column, Integer, String

from database import Base


class Contato(Base):
    __tablename__ = "contatos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(25))
    sobrenome = Column(String(25))
    numerodetelefone = Column(Integer(15))
    email = Column(String(50), unique=True, index=True)
