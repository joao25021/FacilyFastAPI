from sqlalchemy.orm import Session
import models
import schemas


def get_contato(db: Session, contato_id: int):
    return db.query(models.Contato).filter(models.Contato.id == contato_id).first()


def get_contato_by_numero(db: Session, numerodetelefone: str):
    return db.query(models.Contato).filter(models.Contato.numerodetelefone == numerodetelefone).first()


def get_contatos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contato).offset(skip).limit(limit).all()


def create_contato(db: Session, contato):
    db_contato = models.Contato(nome=contato.nome,
                                sobrenome=contato.sobrenome,
                                numerodetelefone=contato.numerodetelefone,
                                email=contato.email
                                )
    db.add(db_contato)
    db.commit()
    db.refresh(db_contato)
    return db_contato


def put_contato(db: Session, contatoAtual, contato):
    contatoAtual.nome = contato.nome
    contatoAtual.sobrenome = contato.sobrenome
    contatoAtual.numerodetelefone = contato.numerodetelefone
    contatoAtual.email = contato.email
    db.commit()
    db.refresh(contatoAtual)
    return contatoAtual


def delete(contato_db, db):
    db.delete(contato_db)
    db.commit()
    return contato_db