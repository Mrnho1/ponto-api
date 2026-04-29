from sqlalchemy.orm import Session
from app.models.ajuste_model import AjusteManual

def criar_ajuste(db: Session, ponto_id, nova_data, motivo):
    ajuste = AjusteManual(
        ponto_id=ponto_id,
        nova_data=nova_data,
        motivo=motivo
    )
    db.add(ajuste)
    db.commit()
    db.refresh(ajuste)
    return ajuste

def listar_ajustes(db: Session):
    return db.query(AjusteManual).all()