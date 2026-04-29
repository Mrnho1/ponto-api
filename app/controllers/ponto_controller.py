from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services import ponto_service
from app.schemas.ponto_schema import PontoAjustadoResponse, PontoResponse

router = APIRouter(prefix="/pontos", tags=["Pontos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Registra ponto
@router.post("/")
def registrar(db: Session = Depends(get_db)):
    return ponto_service.registrar_ponto(db)

#Mostra histórico
@router.get("/historico", response_model=list[PontoResponse])
def historico(db: Session = Depends(get_db)):
    return ponto_service.buscar_todos_pontos(db)

#Mostra banco de horas
@router.get("/banco")
def banco(db: Session = Depends(get_db)):
    return ponto_service.calcular_banco_horas(db)


#Lista pontos brutos
@router.get("/", response_model=list[PontoResponse])
def listar(db: Session = Depends(get_db)):
    return ponto_service.buscar_pontos(db)

#Lista pontos ajustados
@router.get("/ajustados", response_model=list[PontoAjustadoResponse])
def listar_ajustados(db: Session = Depends(get_db)):
    return ponto_service.buscar_pontos_ajustados(db)