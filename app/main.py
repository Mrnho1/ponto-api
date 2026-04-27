from fastapi import FastAPI
from app.core.database import Base, engine
from app.controllers import ponto_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Ponto Eletrônico")

app.include_router(ponto_controller.router)