from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from app.core.database import Base
#Representa uma tabela no banco
class Ponto(Base):
    __tablename__ = "pontos" #Nome tabela

    id = Column(Integer, primary_key=True, index=True) 
    data_hora = Column(DateTime, default=datetime.utcnow)