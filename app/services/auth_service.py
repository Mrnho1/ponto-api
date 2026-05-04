from fastapi import HTTPException

from app.models.user_model import Role, User
from app.repositories import user_repository
from app.core.security import hash_password, verify_password, criar_token


def registrar(db, username, password, role):
    role_enum = Role[role.upper()]

    hashed = hash_password(password)

    user = User(
        username=username,
        password=hashed,
        role=role_enum
    )

    return user_repository.criar_usuario(db, user)


def login(db, username, password):
    user = user_repository.buscar_por_username(db, username)

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = criar_token({
        "sub": user.username,
        "role": user.role.value
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }