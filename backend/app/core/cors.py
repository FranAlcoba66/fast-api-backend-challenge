from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.core.config import settings

def setup_cors(app: FastAPI) -> None:
    """
    Configura CORS en la aplicación FastAPI usando la lista de orígenes permitidos
    definida en settings.
    """

    origins = settings.BACKEND_CORS_ORIGINS

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
