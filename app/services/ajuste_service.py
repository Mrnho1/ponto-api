from sqlalchemy.orm import Session
from app.repositories import ajuste_repository

def registrar_ajuste(db: Session, ponto_id, nova_data, motivo):
    return ajuste_repository.criar_ajuste(db, ponto_id, nova_data, motivo)