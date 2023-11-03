from fastapi import FastAPI
from core.config import setting

def start_application():
    app = FastAPI(title=setting.PROJECT_TITLE, version=setting.PROJECT_VERSION)
    return app

app = start_application()


@app.get('/')
def home():
    return {'msg': 'Suriyaaaa da'}
