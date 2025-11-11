 [![CircleCI](https://dl.circleci.com/status-badge/img/circleci/519hynSWEPShqqHZR5AauT/KaqAvU5nFL3tjPFFfXZuur/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/519hynSWEPShqqHZR5AauT/KaqAvU5nFL3tjPFFfXZuur/tree/main)

# FastAPI Clean Architecture Challenge

This project is a FastAPI application built with clean architecture principles, featuring user management and PostgreSQL database integration.

## Tech Stack

- **Backend Framework**: FastAPI v0.119.0
- **Database**: PostgreSQL 14
- **ORM**: SQLAlchemy v2.0
- **Migration Tool**: Alembic v1.17
- **Package Manager**: Poetry
- **Python Version**: >=3.13
- **Testing**: pytest, pytest-asyncio
- **API Client**: httpx

## Project Structure

```
backend/
├── alembic/             # Database migrations
├── app/
│   ├── core/           # Core application components
│   └── modules/        # Feature modules
│       ├── auth/       # Authentication module
│       ├── pokemon/    # Pokemon module
│       └── user/       # User module
└── tests/              # Test suites
```

## Features

- Clean Architecture implementation
- User Management System
- PostgreSQL Database Integration
- Docker Containerization
- Automated Testing
- CORS Support
- Environment Configuration
- API Documentation (Swagger UI)
 - CI with CircleCI (build + tests)

## Prerequisites

- Docker and Docker Compose
- Python 3.13 or higher
- Poetry (Python package manager)

## Getting Started (Local)

1. **Clone the repository**

```bash
git clone <repository-url>
cd Challenge
```

2. **Environment Setup (.env)**

Create a `.env` file in the `backend` directory with the following variables:

```env
APP_NAME=Challenge
APP_ENV=local
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000

POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=challenge

# SQLAlchemy URL used by the app
DATABASE_URL=postgresql://user:password@db:5432/challenge

PROJECT_NAME=Challenge API
VERSION=0.1.0
API_V1_STR=/api/v1

SECRET_KEY=dev-secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

DB_POOL_SIZE=5
DB_MAX_OVERFLOW=10
DB_POOL_TIMEOUT=30
DB_POOL_RECYCLE=1800

POKEMON_API_URL=https://pokeapi.co/api/v2
```

3. **Start the Application (Docker)**

```bash
docker-compose up -d
```

This will start:
- PostgreSQL database on port 5432
- FastAPI application on port 8000

4. **Access the Application**

- API Documentation: http://localhost:8000/docs
- API Base URL: http://localhost:8000/api/v1

## Development

### Running Tests
You can run tests in two formas:

1) Directamente con Poetry (requiere Postgres corriendo):
```bash
cd backend
poetry install
export DATABASE_URL="postgresql://user:password@localhost:5432/challenge"
poetry run pytest -vv --disable-warnings
```

2) Usando Docker Compose de tests:
```bash
docker compose -f docker-compose.test.yml up --build --abort-on-container-exit --exit-code-from tests
```
Esto levantará un Postgres y ejecutará `pytest` dentro de un contenedor con Poetry.

### Database Migrations

```bash
# Generate a new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head
```

### Running the API locally (hot-reload)
Dentro del contenedor, el backend usa Uvicorn con `--reload`:
```bash
docker-compose up -d
# logs
docker-compose logs -f api
```
Para desarrollo sin Docker:
```bash
cd backend
poetry install
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Continuous Integration (CircleCI)
- El pipeline en `/.circleci/config.yml` usa el orb oficial de Python para:
  - Instalar dependencias con Poetry.
  - Levantar Postgres como servicio.
  - Ejecutar `pytest` apuntando a Postgres.
- Badge de estado al inicio del README.
- Documentación oficial de referencia: `https://circleci.com/docs/guides/getting-started/language-python/`

## API Endpoints

- `GET /`: Health check endpoint
- `GET /api/v1/users`: User-related endpoints
- `POST /api/v1/users/`
- `GET /api/v1/users/{user_id}`
- `PUT /api/v1/users/{user_id}`
- `DELETE /api/v1/users/{user_id}`

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## Author

- **FranAlcoba66** - [GitHub Profile](https://github.com/FranAlcoba66)
- Email: franciscoadrianalcoba@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE file for details.
