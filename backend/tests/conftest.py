import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.base import Base
from app.modules.user.models import User

# 📌 URL de base de datos de prueba (SQLite en memoria)
TEST_DATABASE_URL = "postgresql+psycopg2://test_user:test_password@test_db:5432/test_challenge"


# 🛠️ Engine y Session
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)

# ---------------------------------------------------------
# 🏗️  SETUP GLOBAL - se ejecuta una sola vez antes de todos los tests
# 🧼  CLEAN GLOBAL - se ejecuta al final de toda la suite de tests
# ---------------------------------------------------------
@pytest.fixture(scope="session", autouse=True)
def _global_test_database():
    """Crea la estructura de la DB de prueba antes de toda la suite."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# ---------------------------------------------------------
# 🧪  SETUP / CLEAN POR TEST
# ---------------------------------------------------------
@pytest.fixture(scope="function")
def db_session():
    """Sesión de DB limpia por test usando transacción."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()