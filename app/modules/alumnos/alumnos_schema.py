from pydantic import BaseModel

class CreateAlumnosSchema(BaseModel):
    nombre: str
    appellidoPaterno: str
    apellidoMaterno: str
    edad: int
    usuario: str
    password: str
    