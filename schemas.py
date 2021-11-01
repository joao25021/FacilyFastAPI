from pydantic import BaseModel


class ContatoBase(BaseModel):
    id: int
    numerodetelefone: int
    nome: str
    sobrenome: str
    email: str

    class Config:
        orm_mode = True


class ContatoCreate(BaseModel):
    numerodetelefone: int
    nome: str
    sobrenome: str
    email: str


class Contato(BaseModel):
    id: int


