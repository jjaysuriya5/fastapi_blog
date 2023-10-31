import os
from dotenv import load_dotenv

script_dir = os.path.dirname(__file__)
dotenv_path = os.path.join(script_dir, '../.env')
load_dotenv(dotenv_path=dotenv_path)
class Settings:
    PROJECT_TITLE: str = 'Suriyaa'
    PROJECT_VERSION: str = '1.0.0'

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER','localhost')
    POSTGRES_PORT: int = os.getenv('POSTGRES_PORT',5432)
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    POSTGRES_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

setting = Settings()