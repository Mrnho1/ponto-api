from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from app.core.database import Base

class AjusteManual(Base):
    __tablename__ = "ajustes"

    id = Column(Integer, primary_key=True, index=True)
    

    ponto_id = Column(Integer, ForeignKey("pontos.id"), nullable=False)
    nova_data = Column(DateTime, nullable=False)
    motivo = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    criado_em = Column(DateTime, default=datetime.now)

    ponto = relationship("Ponto")
    