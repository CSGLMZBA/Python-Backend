from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

from app.modules.auth.auth_routes import router as auth_router
from app.modules.alumnos.alumnos_routes import router as alumnos_router
from app.shared.middleware.error_handler import register_exception_handler

load_dotenv()
app = FastAPI()
origins = os.getenv("CORS_ORIGIN").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handler(app)

@app.get("/api/health")
def health():
    return {
        "message": "Servidor funcionando con python ",
        "ok": True
    }

app.include_router(auth_router, prefix="/api/auth")
app.include_router(alumnos_router, prefix="/api/alumnos")