from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.ajuste_schema import AjusteRequest
from app.services import ajuste_service
from datetime import datetime
from app.core.security import admin_only

router = APIRouter(prefix="/ajustes", tags=["Ajustes"])

@router.post("/")
def criar_ajuste(
    ajuste: AjusteRequest,
    db: Session = Depends(get_db),
    user = Depends(admin_only)
):
    return ajuste_service.registrar_ajuste(
        db,
        ajuste.ponto_id,
        ajuste.nova_data,
        ajuste.motivo
    )