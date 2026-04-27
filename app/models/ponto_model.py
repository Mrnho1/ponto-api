from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from app.core.database import Base

class Ponto(Base):
    __tablename__ = "pontos"

    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, default=datetime.utcnow)