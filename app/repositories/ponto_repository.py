from sqlalchemy.orm import Session
from app.models.ponto_model import Ponto

def criar_ponto(db: Session):
    ponto = Ponto()
    db.add(ponto) #Adiciona no banco
    db.commit() #Salva no banco
    db.refresh(ponto) #Atualiza os objetos no Banco
    return ponto

def listar_pontos(db: Session):
    return db.query(Ponto).all()