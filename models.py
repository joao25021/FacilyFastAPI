from sqlalchemy import Column, Integer, String

from database import Base


class Contato(Base):
    __tablename__ = "contatos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(25), unique=True)
    sobrenome = Column(String(25))
    numerodetelefone = Column(Integer)
    email = Column(String(50), unique=True, index=True)

