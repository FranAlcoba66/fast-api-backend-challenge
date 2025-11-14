import os
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.core.base import Base

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
TEST_DATABASE_NAME = os.getenv("TEST_DATABASE_NAME")
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")
ADMIN_DATABASE_URL = os.getenv("ADMIN_DATABASE_URL")
DEBUG_DB = os.getenv("DEBUG_TEST_DB", "false").lower() == "true"


admin_engine = create_engine(ADMIN_DATABASE_URL, isolation_level="AUTOCOMMIT")
test_engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=test_engine)

# -----------------------------
# Fixture global de la DB de test
# -----------------------------
@pytest.fixture(scope="session", autouse=True)
def _global_test_database():
    """Crea la base y las tablas automáticamente si no existen, mantiene visibilidad para debug."""
    with admin_engine.connect() as conn:

        exists = conn.execute(
            text(f"SELECT 1 FROM pg_database WHERE datname = :db"), {"db": TEST_DATABASE_NAME}
        ).scalar()

        if not exists:
            print(f"🧱 Creando base de datos de test: {TEST_DATABASE_NAME}")
            conn.execute(
                text(f'CREATE DATABASE "{TEST_DATABASE_NAME}" OWNER "{POSTGRES_USER}"')
            )

    print("🧱 Creando tablas del modelo en la base de test...")
    Base.metadata.create_all(bind=test_engine)
    yield
    if not DEBUG_DB:
        Base.metadata.drop_all(bind=test_engine)
        print("🧹 Base de datos de test limpiada")
    else:
        print("🧹 Base de test visible para DBeaver")

# -----------------------------
# Fixture por test
# -----------------------------
@pytest.fixture(scope="function")
def db_session():
    """Sesión limpia por test usando transacciones, con impresión de la DB actual."""
    print(f"🧪 Usando base de datos de test: {TEST_DATABASE_URL}")
    connection = test_engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    # Mostrar la base actual dentro del test
    current_db = session.execute(text("SELECT current_database();")).scalar()
    print(f"💾 Test ejecutando en la DB: {current_db}")

    try:
        yield session
        if not DEBUG_DB:
            transaction.rollback()
        else:
            print("🧪 DEBUG MODE: transacciones no se revierten, datos visibles")
    finally:
        session.close()
        connection.close()
