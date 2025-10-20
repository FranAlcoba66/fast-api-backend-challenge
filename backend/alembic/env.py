from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import importlib
import pkgutil

from app.core.config import settings
from app.core.base import Base  # tu Base compartida

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# -------------------------------
# Autoimport de todos los modelos
# -------------------------------
def import_submodules(package_name):
    """Importa todos los submódulos de un paquete para que Base.metadata los detecte."""
    package = importlib.import_module(package_name)
    for _, name, is_pkg in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
        importlib.import_module(name)
        if is_pkg:
            import_submodules(name)

# Importa todos los módulos dentro de app.modules
import_submodules("app.modules")

# -------------------------------
# Metadata de Alembic
# -------------------------------
target_metadata = Base.metadata

# -------------------------------
# Modo offline
# -------------------------------
def run_migrations_offline():
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# -------------------------------
# Modo online
# -------------------------------
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        url=settings.DATABASE_URL,
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

# -------------------------------
# Ejecutar según modo
# -------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
