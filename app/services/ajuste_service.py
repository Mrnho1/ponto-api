from sqlalchemy.orm import Session
from app.repositories import ajuste_repository, ponto_repository
from fastapi import HTTPException

def registrar_ajuste(db, ponto_id, nova_data, motivo):
    ponto = ponto_repository.buscar_por_id(db, ponto_id)

    if not ponto:
        raise HTTPException(status_code=404, detail="Ponto não encontrado")

    return ajuste_repository.criar_ajuste(db, ponto_id, nova_data, motivo)