from pydantic import BaseModel
from datetime import datetime
from app.models.tipo_ponto import TipoPonto

class PontoResponse(BaseModel):
    id: int
    data_hora: datetime
    tipo: TipoPonto

    class Config:
        from_attributes = True


class PontoAjustadoResponse(BaseModel):
    id: int
    data_original: datetime
    data_ajustada: datetime
    tipo: TipoPonto