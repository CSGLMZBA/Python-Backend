from fastapi import APIRouter, Request
from app.modules.alumnos.alumnos_schema import CreateAlumnosSchema
from app.modules.alumnos.alumnos_service import AlumnosService
from app.shared.middleware.auth import verify_token

router = APIRouter()
@router.get("/")
async def get_all(request: Request):
    await verify_token(request)
    service = AlumnosService()
    return service.get_all()

@router.post("/")
async def create(data: CreateAlumnosSchema, request: Request):
    await verify_token(request)
    service = AlumnosService()
    id = service.create(data)
    return {
        "id": id
    }

@router.patch("/{id}")
async def update(id: str, data: CreateAlumnosSchema, request: Request):
    await verify_token(request)
    service = AlumnosService()
    service.update(id,data)
    return {
        "message": "Alumno Actualizado"
    }

@router.delete("/{id}")
async def delete(id:str, request:Request):
    await verify_token(request)
    service = AlumnosService()
    service.delete(id)
    return{
        "message": "Alumno eliminado"
    }