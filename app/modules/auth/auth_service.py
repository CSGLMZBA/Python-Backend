from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.modules.auth.auth_repository import AuthRepository
from app.core.env import JWT_SECRET
from app.shared.utils.api_error import ApiError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def login(self, usuario, password):
        repo = AuthRepository()
        user = repo.find_by_usuario(usuario)

        if not user:
            raise ApiError(401, "Usuario no encontrado")
        
        if not pwd_context.verify(password, user["passwordHash"]):
            raise ApiError(401, "Contraseña incorrecta")
        
        token = jwt.encode(
            {
                "id": user["id"],
                "usuario": user["usuario"],
                "exp": datetime.utcnow() + timedelta(hours=1)
            },
            JWT_SECRET,
            algorithm="HS256")
        return {"token": token}