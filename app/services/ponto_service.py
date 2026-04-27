from sqlalchemy.orm import Session
from app.repositories import ponto_repository

def registrar_ponto(db: Session):
    return ponto_repository.criar_ponto(db)

def buscar_pontos(db: Session):
    return ponto_repository.listar_pontos(db)