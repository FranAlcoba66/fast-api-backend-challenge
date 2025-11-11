# tests/test_user_service.py
import pytest
from app.modules.user.repository import UserRepository



def test_create_two_users(db_session):
    repo = UserRepository()

    # Crear primer usuario
    user1 = repo.create(
        db_session,
        name="User One",
        email="one@example.com",
        pokemon_ids=[1, 2]
    )

    # Crear segundo usuario
    user2 = repo.create(
        db_session,
        name="User Two",
        email="two@example.com",
        pokemon_ids=[3, 4]
    )

    # 📌 GET ALL
    result = repo.get_all(db_session)

    # 🖨️ Print de debugging
    for u in result:
        print({
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "pokemon_ids": u.pokemon_ids
        })

    # ✅ Asserts
    assert len(result) == 2

    assert any(u.email == "one@example.com" for u in result)
    assert any(u.email == "two@example.com" for u in result)

    assert any(u.name == "User One" for u in result)
    assert any(u.name == "User Two" for u in result)



def test_update_user(db_session):
    repo = UserRepository()

    # Crear primer usuario
    user1 = repo.create(
        db_session,
        name="User One",
        email="one@example.com",
        pokemon_ids=[1, 2]
    )

    # Crear segundo usuario
    user2 = repo.create(
        db_session,
        name="User Two",
        email="two@example.com",
        pokemon_ids=[3, 4]
    )

    # 📌 GET ALL
    result = repo.get_all(db_session)

    # 🖨️ Print de debugging
    for u in result:
        print({
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "pokemon_ids": u.pokemon_ids
        })

    # ✅ Asserts
    assert len(result) == 2

    assert any(u.email == "one@example.com" for u in result)
    assert any(u.email == "two@example.com" for u in result)

    assert any(u.name == "User One" for u in result)
    assert any(u.name == "User Two" for u in result)
