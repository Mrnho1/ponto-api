from sqlalchemy.orm import Session
from app.repositories import ajuste_repository, ponto_repository
from fastapi import HTTPException

def registrar_ajuste(db, ponto_id, nova_data, motivo, admin_user):
    ponto = ponto_repository.buscar_por_id(db, ponto_id)

    if not ponto:
        raise HTTPException(status_code=404, detail="Ponto não encontrado")

    # salva histórico
    ajuste_repository.criar_ajuste(db, ponto_id, nova_data, motivo)

    # atualiza ponto real
    ponto.data_hora = nova_data
    db.commit()
    db.refresh(ponto)

    return {
        "mensagem": "Ajuste aplicado com sucesso",
        "ponto_id": ponto.id,
        "nova_data": ponto.data_hora,
        "motivo": motivo,
        "ajustado_por": admin_user["sub"]
    }

def listar_ajustes(db):
    return ajuste_repository.listar_ajustes(db)