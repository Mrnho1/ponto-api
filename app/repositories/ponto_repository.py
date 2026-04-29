from datetime import datetime, time

from app.models.ponto_model import Ponto
from sqlalchemy.orm import Session
from app.repositories import ajuste_repository, ponto_repository


def criar_ponto(db: Session, tipo):
    ponto = Ponto(tipo=tipo)
    db.add(ponto)
    db.commit()
    db.refresh(ponto)
    return ponto

def listar_pontos_do_dia(db: Session):
    hoje = datetime.now().date()

    inicio = datetime.combine(hoje, time.min)  
    fim = datetime.combine(hoje, time.max)    

    return db.query(Ponto).filter(
    Ponto.data_hora >= inicio,
    Ponto.data_hora <= fim
    ).order_by(Ponto.data_hora).all()
    
def listar_todos_pontos(db: Session):
    return db.query(Ponto).order_by(Ponto.data_hora).all()

def calcular_horas_trabalhadas(db: Session):
    pontos = ponto_repository.listar_pontos_do_dia(db)
    ajustes = ajuste_repository.listar_ajustes(db)

    # 🔥 Criar mapa de ajustes
    mapa_ajustes = {a.ponto_id: a.nova_data for a in ajustes}

    # 🔥 Aplicar ajustes
    for p in pontos:
        if p.id in mapa_ajustes:
            p.data_hora = mapa_ajustes[p.id]

    if len(pontos) < 4:
        return {"mensagem": "Jornada incompleta"}

    entrada = pontos[0].data_hora
    saida_almoco = pontos[1].data_hora
    volta_almoco = pontos[2].data_hora
    saida = pontos[3].data_hora

    periodo_manha = saida_almoco - entrada
    periodo_tarde = saida - volta_almoco

    total = periodo_manha + periodo_tarde

    return {
        "horas_trabalhadas": str(total)
    }