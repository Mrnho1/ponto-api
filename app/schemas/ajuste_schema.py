from pydantic import BaseModel
from datetime import datetime

class AjusteRequest(BaseModel):
    ponto_id: int
    nova_data: datetime
    motivo: str