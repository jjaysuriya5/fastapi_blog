from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import setting
from typing import Generator

SQLALCHEMY_DATABASE_URL = setting.POSTGRES_URL
print('Database URL is',SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
# engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})

SESSIONLOCAL = sessionmaker(autoflush=False, autocommit=False , bind=engine)

def get_db() -> Generator:
    try:
        db = SESSIONLOCAL()
        yield db
    finally:
        db.close()
