# tests/test_user_service.py
import pytest
from app.modules.user.service import UserService
from app.modules.user.repository import UserRepository
from app.modules.user.models import User
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_get_user_by_id(db_session):
    # 1️⃣ Crear usuario de prueba
    repo = UserRepository()
    user = repo.create(
        db_session,
        name="Test User",
        email="test@example.com",
        pokemon_ids=[1, 2, 3]
    )

    # 2️⃣ Crear servicio y mockear el cliente Pokémon
    service = UserService(repository=repo)
    service._pokemon_client.get_multiple_pokemon_names = AsyncMock(return_value=[
        {"id": 1, "name": "Bulbasaur"},
        {"id": 2, "name": "Ivysaur"},
        {"id": 3, "name": "Venusaur"},
    ])

    # 3️⃣ Ejecutar la función
    result = await service.get_user_by_id(db_session, user.id)

    # 4️⃣ Verificaciones
    assert result["id"] == user.id
    assert result["name"] == user.name
    assert result["email"] == user.email
    assert result["pokemon_ids"] == [1, 2, 3]
    assert result["pokemons"] == [
        {"id": 1, "name": "Bulbasaur"},
        {"id": 2, "name": "Ivysaur"},
        {"id": 3, "name": "Venusaur"},
    ]

@pytest.mark.asyncio
async def test_get_user_by_id_not_found(db_session):
    repo = UserRepository()
    service = UserService(repository=repo)

    # Se espera que lance ValueError si no existe el usuario
    with pytest.raises(ValueError) as e:
        await service.get_user_by_id(db_session, user_id=999)
    assert "no encontrado" in str(e.value)
