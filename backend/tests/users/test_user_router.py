# tests/test_user_router_sync.py
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock

from app.modules.user.router import router, get_user_service
from app.modules.user.service import UserService

# 🔹 Crear app de prueba e incluir el router
app = FastAPI()
app.include_router(router, prefix="/users", tags=["users"])

@pytest.fixture
def mock_user_service():
    service = UserService(repository=None)  # repository no se usará por el mock
    # Mockear el método asíncrono get_user_by_id
    service.get_user_by_id = AsyncMock(return_value={
        "id": 1,
        "name": "Test User",
        "email": "test@example.com",
        "pokemon_ids": [1, 2],
        "pokemons": [
            {"id": 1, "name": "Bulbasaur"},
            {"id": 2, "name": "Ivysaur"},
        ]
    })
    return service

# 🔹 TestClient síncrono
@pytest.fixture
def client(mock_user_service):

    app.dependency_overrides[get_user_service] = lambda: mock_user_service
    return TestClient(app)

def test_get_user_by_id_endpoint(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"
    assert data["pokemon_ids"] == [1, 2]
    assert data["pokemons"] == [
        {"id": 1, "name": "Bulbasaur"},
        {"id": 2, "name": "Ivysaur"},
    ]

def test_get_user_by_id_not_found_endpoint(client, mock_user_service):
    # Hacer que el mock lance ValueError
    mock_user_service.get_user_by_id.side_effect = ValueError("Usuario con ID 999 no encontrado")
    
    response = client.get("/users/999")
    assert response.status_code == 404
    assert "no encontrado" in response.json()["detail"]
