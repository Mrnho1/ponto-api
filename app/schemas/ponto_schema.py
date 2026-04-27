from pydantic import BaseModel
from datetime import datetime
#Modo de resposta da API
class PontoResponse(BaseModel):
    id: int
    data_hora: datetime
    #Igual ao mapStruct
    class Config:
        orm_mode = True #Permite converter automaticamente do model