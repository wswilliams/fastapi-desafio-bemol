from fastapi import FastAPI

from app.api import clientes
from app.models.model_cliente import Base
from app.database.db import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(clientes.router, prefix="/clientes", tags=["clientes"])
