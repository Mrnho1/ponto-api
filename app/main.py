from fastapi import FastAPI
from app.core.database import Base, engine
from app.controllers import ajuste_controller, ponto_controller
#Manda criar as tabelas no banco com base nos models
Base.metadata.create_all(bind=engine)

#Aqui iremos criar a aplicação
app = FastAPI(title="API de Ponto Eletrônico")
#Conecta os endpoints na aplicação
app.include_router(ponto_controller.router)
app.include_router(ajuste_controller.router)