# -----------------------------------------------------------
# STAGE 1: Base - Python 3.13
# -----------------------------------------------------------
FROM python:3.13-slim AS base

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    libffi-dev \
    libssl-dev \
 && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Agregar Poetry al PATH
ENV PATH="/root/.local/bin:$PATH"

# Crear directorio de trabajo y copiar proyecto
WORKDIR /app
COPY . .

# -----------------------------------------------------------
# STAGE 2: Backend dependencies
# -----------------------------------------------------------
WORKDIR /app/backend
# Instalar dependencias definidas en pyproject.toml
RUN poetry install --no-root --no-interaction --no-ansi

# -----------------------------------------------------------
# STAGE 3: Configuración final
# -----------------------------------------------------------
WORKDIR /app/backend
EXPOSE 8000

# Ejecutar FastAPI usando Uvicorn dentro del virtualenv de Poetry

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]