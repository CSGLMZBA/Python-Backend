from passlib.context import CryptContext
from datetime import datetime
from app.modules.alumnos.alumnos_repository import AlumnosRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AlumnosService:
    def get_all(self):
        repo = AlumnosRepository()
        return repo.get_all()
    def create(self,data):
        repo = AlumnosRepository()
        hashed = pwd_context.hash(data.password)
        alumno = {
            "nombre": data.nombre,
            "apellidoMaterno": data.apellidoMaterno,
            "apellidoPaterno": data.apellidPaterno,
            "nombreCompleto": f"{data.nombre} {data.apellidoPaterno} {data.apellidoMaterno}",
            "edad": data.edad,
            "usuario": data.usuario,
            "passwordHash": hashed,
            "activo": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        }
        return repo.create(alumno)
    
    def update(self,id,data):
        repo = AlumnosRepository()
        repo.update(id,data.dict())
    
    def delete(self, id):
        repo = AlumnosRepository()
        repo.delete(id)