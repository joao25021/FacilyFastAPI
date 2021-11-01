from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, db_engine

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/contato/",
          response_model=schemas.ContatoCreate,
          description="Criar um novo contato",
          status_code=status.HTTP_201_CREATED,
          responses={400: {"description": "Numero de telefone{NUMERO} esta já registrado"}})
def create_contato(contato: schemas.ContatoCreate, db: Session = Depends(get_db)):
    db_contato = crud.get_contato_by_numero(db, numerodetelefone=contato.numerodetelefone)
    if db_contato:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Numero de telefone {contato.numerodetelefone} esta já registrado")
    return crud.create_contato(db=db, contato=contato)


@app.get("/contatos/",
         response_model=List[schemas.ContatoBase],
         status_code=status.HTTP_200_OK)
def list_contato(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contatos = crud.get_contatos(db, skip=skip, limit=limit)
    return contatos


@app.get("/contatos/{contato_id}",
         response_model=schemas.Contato,
         description="Procurar contato pelo id",
         responses={404: {"description": "Contato não encontrado"}})
def read_contato(contato_id: int, db: Session = Depends(get_db)):
    db_contato = crud.get_contato(db, contato_id=contato_id)
    if db_contato is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contato não encontrado")
    return db_contato


@app.put("/contatos/{contato_id}",
         tags=["contatos"],
         response_model=schemas.ContatoBase,
         description="Update contato pelo Id",
         responses={404: {"description": "Contato não encontrado"}})
def update_contato(contato_id: int, contato: schemas.ContatoCreate, db: Session = Depends(get_db)):
    contatoAtual = read_contato(contato_id, db)
    db_contato = crud.put_contato(db, contatoAtual, contato)
    return db_contato


@app.delete('/contatos/{contato_id}',
            response_model=schemas.ContatoBase,
            description="Update contato pelo Id",
            responses={404: {"description": "Contato não encontrado"}})
def delete_users(contato_id: int, db: Session = Depends(get_db)):
    contato_db = read_contato(contato_id, db)
    db_contato = crud.delete(contato_db, db)
    return db_contato
