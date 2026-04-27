from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services import ponto_service
from app.schemas.ponto_schema import PontoResponse

router = APIRouter(prefix="/pontos", tags=["Pontos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def registrar(db: Session = Depends(get_db)):
    return ponto_service.registrar_ponto(db)

@router.get("/", response_model=list[PontoResponse])
def listar(db: Session = Depends(get_db)):
    return ponto_service.buscar_pontos(db)