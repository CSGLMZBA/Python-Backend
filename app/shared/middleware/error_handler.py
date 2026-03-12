from fastapi.responses import JSONResponse
from fastapi import Request
from app.shared.utils.api_error import ApiError

def register_exception_handler(app):
    @app.exception_handler(ApiError)
    async def api_error_handler(request: Request, exc: ApiError):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.message},
        )
    
    @app.exception_handler(Exception)
    async def global_error(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"message": "Error interno del servidor"},
        )