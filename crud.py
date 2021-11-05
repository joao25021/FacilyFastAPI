from sqlalchemy.orm import Session
import models
import schemas


def get_contato(db: Session, contato_id: int):
    """ Realizar a busca de contato no banco por id

            - **db**: Session do banco
            - **contato_id**:(int) required
            \f
            :param contato_id:
            :param db: interação com o banco (Session)

            :return: contato ou null
                    """
    return db.query(models.Contato).filter(models.Contato.id == contato_id).first()


def get_contato_by_numero(db: Session, numerodetelefone: str):
    """ Realizar a busca no banco por numero de telefone

                - **db**: Session do banco
                - **numero de telefone**: (str) required
                \f
                :param numerodetelefone: str
                :param db: interação com o banco (Session)

                :return: contato ou null
                        """
    return (
        db.query(models.Contato)
        .filter(models.Contato.numerodetelefone == numerodetelefone)
        .first()
    )


def get_contatos(db: Session, skip: int = 0, limit: int = 100):
    """ Realizar a busca de com intervalor skip até limit

            - **skip**:(int) required - valor padrão: 0
            - **limit**:(int) required - valor padrão: 100
            \f
            :param limit: 100
            :param skip: 0
            :param db: interação com o banco (Session)

            :return: list contatos
                """
    return db.query(models.Contato).offset(skip).limit(limit).all()


def create_contato(db: Session, contato):
    """ Realizar a criação de um contato no banco

                    - **db**: Session do banco
                    - **contato**: schema para um contato
                    \f
                    :param contato: schema para um contato
                    :param db: interação com o banco (Session)

                    :return: contato ou null
                            """
    db_contato = models.Contato(
        nome=contato.nome,
        sobrenome=contato.sobrenome,
        numerodetelefone=contato.numerodetelefone,
        email=contato.email,
    )
    db.add(db_contato)
    db.commit()
    db.refresh(db_contato)
    return db_contato


def put_contato(db: Session, contatoAtual, contato):
    """ Realizar a atualizaçao de um contato no banco

                        - **db**: Session do banco
                        - **contatoAtual**: contato (antigo)
                        - **contato**: contato (informações novas)
                        \f
                        :param contatoAtual: valor a ser atualizado
                        :param contato: informações novas
                        :param db: interação com o banco (Session)

                        :return: contato alterado
                                """
    contatoAtual.nome = contato.nome
    contatoAtual.sobrenome = contato.sobrenome
    contatoAtual.numerodetelefone = contato.numerodetelefone
    contatoAtual.email = contato.email
    db.commit()
    db.refresh(contatoAtual)
    return contatoAtual


def delete(contato_db, db):
    """ Realizar a delete de um conto no banco

                        - **db**: Session do banco
                        - **contato_db**: referencia do contato no db
                        \f
                        :param contato_db:schema para um contato
                        :param db: interação com o banco (Session)

                        :return: contato ou null
                                """
    db.delete(contato_db)
    db.commit()
    return contato_db
