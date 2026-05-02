from datetime import datetime, time
from sqlalchemy.orm import Session
from app.models.ponto_model import Ponto


def criar_ponto(db: Session, tipo, user_id):
    ponto = Ponto(tipo=tipo, user_id=user_id)
    db.add(ponto)
    db.commit()
    db.refresh(ponto)
    return ponto


def listar_pontos_do_dia_por_usuario(db: Session, user_id: int):
    hoje = datetime.now().date()

    inicio = datetime.combine(hoje, time.min)
    fim = datetime.combine(hoje, time.max)

    return db.query(Ponto).filter(
        Ponto.user_id == user_id,
        Ponto.data_hora >= inicio,
        Ponto.data_hora <= fim
    ).order_by(Ponto.data_hora).all()


def listar_todos_pontos(db: Session):
    return db.query(Ponto).order_by(Ponto.data_hora).all()


def listar_por_usuario(db: Session, user_id: int):
    return db.query(Ponto).filter(
        Ponto.user_id == user_id
    ).order_by(Ponto.data_hora).all()