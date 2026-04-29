from sqlalchemy import Column, Integer, DateTime, String
from datetime import datetime
from app.core.database import Base

class AjusteManual(Base):
    __tablename__ = "ajustes"

    id = Column(Integer, primary_key=True, index=True)

    ponto_id = Column(Integer, nullable=False)

    nova_data = Column(DateTime, nullable=False)
    motivo = Column(String, nullable=False)

    criado_em = Column(DateTime, default=datetime.now)