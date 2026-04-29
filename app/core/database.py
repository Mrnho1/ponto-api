from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./ponto.db"
#Conecta com o SQLite
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
#Criar sessões, conexões temporárias com o banco
SessionLocal = sessionmaker(bind=engine)
#Base que todos os models herdam
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()