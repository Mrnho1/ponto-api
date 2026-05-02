from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

# 🔐 Configurações
SECRET_KEY = "sua-chave-secreta"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 60

# 🔐 OAuth2 (Swagger vai usar isso automaticamente)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# 🔐 Hash de senha
pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)

# 🔐 Criar token JWT
def criar_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token

# 🔐 Pegar usuário logado (decodifica token)
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username = payload.get("sub")
        role = payload.get("role")

        if username is None or role is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        return {
            "sub": username,
            "role": role
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

# 🔐 Apenas ADMIN
def admin_only(user: dict = Depends(get_current_user)):
    if user.get("role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Acesso negado")

    return user