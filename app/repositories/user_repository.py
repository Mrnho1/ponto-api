from sqlalchemy.orm import Session
from app.models.user_model import User

def buscar_por_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def criar_usuario(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user