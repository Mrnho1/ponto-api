from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(username: str, password: str, role: str, db: Session = Depends(get_db)):
    return auth_service.registrar(db, username, password, role)

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return auth_service.login(db, form_data.username, form_data.password)