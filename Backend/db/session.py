from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Backend.core.config import setting

SQLALCHEMY_DATABASE_URL = setting.POSTGRES_URL
print('Database URL is',SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SESSIONLOCAL = sessionmaker(autoflush=False, autocommit=False , bind=engine)


