from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, criar_bd
from mangum import Mangum

app = FastAPI()

criar_bd()


# Dependency
def get_db():
    """A criação SessionLocal()
    garantimos que a sessão do banco de dados esteja sempre fechada após a solicitação terminar.
    Mesmo se houver uma exceção durante o processamento da solicitação,
    o tratamento das solicitações em um trybloco.
    então fechamos no finallybloco.
        """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(
    "/contato/",
    response_model=schemas.ContatoBase,
    summary="Criar um novo contato",
    status_code=status.HTTP_201_CREATED,
    responses={400: {"description": "Numero de telefone{NUMERO} esta já registrado"}},
)
def create_contato(contato: schemas.ContatoCreate, db: Session = Depends(get_db)):
    """ Criar um novo contato
        - **numerodetelefone**:(str) required
        - **nome**:(str) required
        - **sobrenome**:(str) required
        - **email**:(str) required

        deve retornar um **schemas.ContatoBase**

        Caso ja tenha um numero de telefone igual {400: {"description": "Numero de telefone{NUMERO} esta já registrado"}

        \f
        :param contato: ContatoCreate
        :param db: interação com o banco (Session)

        :return: ContatoBase
                """
    db_contato = crud.get_contato_by_numero(
        db, numerodetelefone=contato.numerodetelefone
    )
    if db_contato:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Numero de telefone {contato.numerodetelefone} esta já registrado",
        )
    return crud.create_contato(db=db, contato=contato)


@app.get(
    "/contatos/",
    response_model=List[schemas.ContatoBase],
    summary="retorna uma lista de contatos",
    status_code=status.HTTP_200_OK,
)
def list_contato(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """ Realizar a busca de uma **lista de contatos**
        deve retornar um **Lista de contatos** (JSON)

        - **skip**:(int) required - valor padrão: 0
        - **limit**:(int) required - valor padrão: 100
        \f
        :param limit: 100
        :param skip: 0
        :param db: interação com o banco (Session)

        :return: list contatos
                """
    contatos = crud.get_contatos(db, skip=skip, limit=limit)
    return contatos


@app.get(
    "/contatos/{contato_id}",
    response_model=schemas.ContatoBase,
    summary="Procurar contato pelo id",
    responses={404: {"description": "Contato não encontrado"}},
)
def read_contato(contato_id: int, db: Session = Depends(get_db)):
    """ Realizar a busca de um contato por **id**
        deve retornar um **schemas.ContatoBase**

        caso não encontre {404: {"description": "Contato não encontrado"}

        - **contato_id**:(int) required
        \f
        :param contato_id: int
        :param db: interação com o banco (Session)

        :return: ContatoBase
                """
    db_contato = crud.get_contato(db, contato_id=contato_id)
    if db_contato is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contato não encontrado"
        )
    return db_contato


@app.put(
    "/contatos/{contato_id}",
    tags=["contatos"],
    response_model=schemas.ContatoBase,
    summary="Update contato pelo Id",
    responses={404: {"description": "Contato não encontrado"}},
)
def update_contato(
        contato_id: int, contato: schemas.ContatoCreate, db: Session = Depends(get_db)
):
    """ Realizar a atualização de um contato por **id**
        - **contato_id**:(int) required

        informações para atualizar (opicinal)
        - **numerodetelefone**:(str)
        - **nome**:(str)
        - **sobrenome**:(str)
        - **email**:(str)

        deve retornar um **schemas.ContatoBase**

        caso não encontre {404: {"description": "Contato não encontrado"}

        \f
        :param contato_id: int
        :param contato: ContatoCreate
        :param db: interação com o banco (Session)

        :return: ContatoBase
                """
    contatoAtual = read_contato(contato_id, db)
    db_contato = crud.put_contato(db, contatoAtual, contato)
    return db_contato


@app.delete(
    "/contatos/{contato_id}",
    response_model=schemas.ContatoBase,
    summary="delete contato pelo Id",
    responses={404: {"description": "Contato não encontrado"}},
)
def delete_users(contato_id: int, db: Session = Depends(get_db)):
    """ Realizar o delete de um contato por **id**
        deve retornar um **schemas.ContatoBase** do contato que foi apagado

        - **contato_id**:(int) required

        caso não encontre {404: {"description": "Contato não encontrado"}

        \f
        :param contato_id: int
        :param db: interação com o banco (Session)

        :return: ContatoBase
                """
    contato_db = read_contato(contato_id, db)
    db_contato = crud.delete(contato_db, db)
    return db_contato


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

handler = Mangum(app=app)
