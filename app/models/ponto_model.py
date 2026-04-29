from sqlalchemy import Column, Integer, DateTime, Enum
from datetime import datetime
from app.core.database import Base
from app.models.tipo_ponto import TipoPonto

class Ponto(Base):
    __tablename__ = "pontos"

    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, default=datetime.now)
    tipo = Column(Enum(TipoPonto), nullable=False)