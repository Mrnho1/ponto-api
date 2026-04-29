from collections import defaultdict
from datetime import timedelta

from sqlalchemy.orm import Session
from app.repositories import ajuste_repository, ponto_repository
from app.models.tipo_ponto import TipoPonto

def registrar_ponto(db: Session):
    pontos_hoje = ponto_repository.listar_pontos_do_dia(db)

    quantidade = len(pontos_hoje)

    if quantidade == 0:
        tipo = TipoPonto.ENTRADA
    elif quantidade == 1:
        tipo = TipoPonto.SAIDA_ALMOCO
    elif quantidade == 2:
        tipo = TipoPonto.VOLTA_ALMOCO
    elif quantidade == 3:
        tipo = TipoPonto.SAIDA
    else:
        raise Exception("Limite de pontos atingido no dia")

    return ponto_repository.criar_ponto(db, tipo)

def buscar_pontos(db: Session):
    pontos = ponto_repository.listar_pontos_do_dia(db)
    ajustes = ajuste_repository.listar_ajustes(db)

    mapa_ajustes = {a.ponto_id: a.nova_data for a in ajustes}

    resultado = []

    for p in pontos:
        resultado.append({
            "id": p.id,
            "data_hora": mapa_ajustes.get(p.id, p.data_hora),
            "tipo": p.tipo
        })

    return resultado


def buscar_pontos_ajustados(db: Session):
    pontos = ponto_repository.listar_pontos_do_dia(db)
    ajustes = ajuste_repository.listar_ajustes(db)

    mapa_ajustes = {a.ponto_id: a.nova_data for a in ajustes}

    resultado = []

    for p in pontos:
        resultado.append({
            "id": p.id,
            "data_original": p.data_hora,
            "data_ajustada": mapa_ajustes.get(p.id, p.data_hora),
            "tipo": p.tipo
        })

    return resultado

def buscar_todos_pontos(db: Session):
    return ponto_repository.listar_todos_pontos(db)

def calcular_banco_horas(db: Session):
    pontos = ponto_repository.listar_todos_pontos(db)
    ajustes = ajuste_repository.listar_ajustes(db)

    mapa_ajustes = {a.ponto_id: a.nova_data for a in ajustes}

    dias = defaultdict(list)

    # Agrupar por dia (com ajuste aplicado)
    for p in pontos:
        data = mapa_ajustes.get(p.id, p.data_hora)
        dia = data.date()
        dias[dia].append((p, data))

    total = timedelta()

    for dia, registros in dias.items():
        if len(registros) == 4:
            # Ordena pelos horários (IMPORTANTE)
            registros.sort(key=lambda x: x[1])

            entrada = registros[0][1]
            saida_almoco = registros[1][1]
            volta_almoco = registros[2][1]
            saida = registros[3][1]

            horas = (saida_almoco - entrada) + (saida - volta_almoco)

            jornada = timedelta(hours=8)

            total += (horas - jornada)

    return {
        "banco_horas": str(total)
    }