from jose import jwt, JWTError
from app.shared.utils.api_error import ApiError
from app.core.env import JWT_SECRET

async def verify_token(request):
    auth = request.headers.get("Authorization")
    if not auth:
        raise ApiError(401,"Token requerido")
    
    try:
        token = auth.split(" ")[1]
        decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        request.state.user_id = decoded
    except JWTError:
        raise ApiError(401,"Token inválido")