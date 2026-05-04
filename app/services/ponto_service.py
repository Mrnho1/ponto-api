from collections import defaultdict
from datetime import timedelta
from sqlalchemy.orm import Session
from app.repositories import ponto_repository, ajuste_repository, user_repository
from app.models.tipo_ponto import TipoPonto


def registrar_ponto(db: Session, username: str):
    user = user_repository.buscar_por_username(db, username)

    pontos_hoje = ponto_repository.listar_pontos_do_dia_por_usuario(db, user.id)

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

    return ponto_repository.criar_ponto(db, tipo, user.id)


# 🔎 LISTAR PONTOS
def buscar_pontos(db: Session, username: str, role: str):
    if role == "ADMIN":
        pontos = ponto_repository.listar_todos_pontos(db)
    else:
        user = user_repository.buscar_por_username(db, username)
        pontos = ponto_repository.listar_pontos_do_dia_por_usuario(db, user.id)

    ajustes = ajuste_repository.listar_ajustes(db)
    mapa = {a.ponto_id: a.nova_data for a in ajustes}

    return [
    {
        "id": p.id,
        "data_hora": p.data_hora,
        "tipo": p.tipo
    }
    for p in pontos
]


# 🔎 AJUSTADOS
def buscar_pontos_ajustados(db: Session, username: str, role: str):
    if role == "ADMIN":
        pontos = ponto_repository.listar_todos_pontos(db)
    else:
        user = user_repository.buscar_por_username(db, username)
        pontos = ponto_repository.listar_pontos_do_dia_por_usuario(db, user.id)

    ajustes = ajuste_repository.listar_ajustes(db)

    mapa = {a.ponto_id: a for a in ajustes}

    return [
        {
            "id": p.id,
            "data_original": mapa[p.id].criado_em if p.id in mapa else p.data_hora,
            "data_ajustada": p.data_hora,
            "tipo": p.tipo
        }
        for p in pontos
    ]


# 🔎 HISTÓRICO
def buscar_todos_pontos(db: Session, role: str, username: str):
    if role == "ADMIN":
        return ponto_repository.listar_todos_pontos(db)

    user = user_repository.buscar_por_username(db, username)
    return ponto_repository.listar_por_usuario(db, user.id)


# 🧮 BANCO DE HORAS
def calcular_banco_horas(db: Session, username: str, role: str):
    if role == "ADMIN":
        pontos = ponto_repository.listar_todos_pontos(db)
    else:
        user = user_repository.buscar_por_username(db, username)
        pontos = ponto_repository.listar_por_usuario(db, user.id)

    ajustes = ajuste_repository.listar_ajustes(db)
    

    dias = defaultdict(list)

    for p in pontos:
        dias[p.data_hora.date()].append(p.data_hora)

    total = timedelta()

    for registros in dias.values():
        if len(registros) == 4:
            registros.sort()

            horas = (registros[1] - registros[0]) + (registros[3] - registros[2])
            jornada = timedelta(hours=8)

            total += (horas - jornada)

    return {"banco_horas": str(total)}