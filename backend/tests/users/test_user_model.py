import pytest
from app.modules.user.models import User

@pytest.mark.usefixtures("db_session")
def test_create_user(db_session):
    """Crear un usuario en la DB de prueba."""
    # 🏗️ Setup
    user = User(name="Fran", email="create_user@test.com")

    # 🧪 Run
    db_session.add(user)
    db_session.commit()

    # ✅ Assert
    saved_user = db_session.query(User).filter_by(email="create_user@test.com").first()
    assert saved_user is not None
    assert saved_user.name == "Fran"


@pytest.mark.usefixtures("db_session")
def test_update_user(db_session):
    """Editar un usuario existente."""
    # 🏗️ Setup: crear usuario inicial
    user = User(name="Fran", email="create_user@test.com")
    db_session.add(user)
    db_session.commit()

    # 🧪 Run: modificar nombre
    user_to_update = db_session.query(User).filter_by(email="create_user@test.com").first()
    user_to_update.name = "Francisco"
    db_session.commit()

    # ✅ Assert
    updated_user = db_session.query(User).filter_by(email="create_user@test.com").first()
    assert updated_user.name == "Francisco"


@pytest.mark.usefixtures("db_session")
def test_delete_user(db_session):
    """Eliminar un usuario existente."""
    # 🏗️ Setup: crear usuario inicial
    user = User(name="Fran", email="delete_user@test.com")
    db_session.add(user)
    db_session.commit()

    # 🧪 Run: eliminar usuario
    db_session.delete(user)
    db_session.commit()

    # ✅ Assert: verificar que ya no existe
    deleted_user = db_session.query(User).filter_by(email="delete_user@test.com").first()
    assert deleted_user is None
