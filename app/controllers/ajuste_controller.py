from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services import ajuste_service
from datetime import datetime


router = APIRouter(prefix="/ajustes", tags=["Ajustes"])

@router.post("/")
def criar_ajuste(
    ponto_id: int,
    nova_data: datetime,
    motivo: str,
    db: Session = Depends(get_db)
):
    return ajuste_service.registrar_ajuste(db, ponto_id, nova_data, motivo)