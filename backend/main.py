from fastapi import FastAPI

from app.core.cors import setup_cors
from app.core.databse import engine
from app.core.config import Settings
# Importa el objeto router del módulo 'user'
from app.modules.user.router import router as user_router
# from app.modules.pokemon.router import router as pokemon_router
app = FastAPI(
    title="Clean Architecture FastAPI Demo",
    version="1.0.0"
)


setup_cors(app)
@app.get("/")
async def read_main():
    return {"msg": "Hello"}
# Incluye el router en la aplicación principal
app.include_router(user_router, prefix="/api/v1/users", tags=["users"])
