from pydantic import BaseModel
from datetime import datetime

class PontoResponse(BaseModel):
    id: int
    data_hora: datetime

    class Config:
        orm_mode = True