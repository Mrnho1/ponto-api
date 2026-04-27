from sqlalchemy.orm import Session
from app.models.ponto_model import Ponto

def criar_ponto(db: Session):
    ponto = Ponto()
    db.add(ponto)
    db.commit()
    db.refresh(ponto)
    return ponto

def listar_pontos(db: Session):
    return db.query(Ponto).all()