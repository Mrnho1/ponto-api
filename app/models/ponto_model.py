from sqlalchemy import Column, ForeignKey, Integer, DateTime, Enum
from datetime import datetime
from app.core.database import Base
from app.models.tipo_ponto import TipoPonto
from sqlalchemy.orm import relationship

class Ponto(Base):
    __tablename__ = "pontos"

    id = Column(Integer, primary_key=True, index=True)
    data_hora = Column(DateTime, default=datetime.now)
    tipo = Column(Enum(TipoPonto), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))  # 🔥 novo campo

    user = relationship("User")    
