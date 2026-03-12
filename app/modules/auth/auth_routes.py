from fastapi import APIRouter
from app.modules.auth.auth_schema import LoginSchema
from app.modules.auth.auth_service import AuthService

router = APIRouter()

@router.post("/login")
def login(data: LoginSchema):
    service = AuthService()
    return service.login(data.usuario, data.password)