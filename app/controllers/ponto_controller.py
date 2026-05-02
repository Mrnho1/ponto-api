from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user
from app.services import ponto_service
from app.schemas.ponto_schema import PontoResponse, PontoAjustadoResponse

router = APIRouter(prefix="/pontos", tags=["Pontos"])

# Registrar ponto (USER ou ADMIN)
@router.post("/")
def registrar(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return ponto_service.registrar_ponto(db, user["sub"])


# Listar pontos do usuário logado
@router.get("/", response_model=list[PontoResponse])
def listar(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return ponto_service.buscar_pontos(db, user["sub"], user["role"])


# Pontos ajustados
@router.get("/ajustados", response_model=list[PontoAjustadoResponse])
def listar_ajustados(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return ponto_service.buscar_pontos_ajustados(db, user["sub"], user["role"])


# Histórico completo (ADMIN vê tudo)
@router.get("/historico")
def historico(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return ponto_service.buscar_todos_pontos(
        db,
        user["role"],
        user["sub"]
    )


# Banco de horas
@router.get("/banco")
def banco(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return ponto_service.calcular_banco_horas(
        db,
        user["sub"],
        user["role"]
    )