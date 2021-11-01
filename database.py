# database.py
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/contatos2"


db_engine = create_engine(SQLALCHEMY_DATABASE_URL)

meta = MetaData()
conn = db_engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
Base = declarative_base()

