# FastAPI Clean Architecture Challenge

[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/519hynSWEPShqqHZR5AauT/KaqAvU5nFL3tjPFFfXZuur/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/519hynSWEPShqqHZR5AauT/KaqAvU5nFL3tjPFFfXZuur/tree/main)
[![Coverage Status](https://coveralls.io/repos/github/FranAlcoba66/fast-api-backend-challenge/badge.svg?branch=main)](https://coveralls.io/github/FranAlcoba66/fast-api-backend-challenge?branch=main)

A modern FastAPI application built with clean architecture principles, featuring user management, PostgreSQL database integration, and comprehensive test coverage. This project demonstrates best practices in API development, including proper separation of concerns, dependency injection, and automated testing.

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Getting Started](#-getting-started)
- [Development](#-development)
- [Testing](#-testing)
- [Database Migrations](#-database-migrations)
- [API Documentation](#-api-documentation)
- [Continuous Integration](#-continuous-integration)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **Clean Architecture**: Well-structured codebase following clean architecture principles
- **User Management**: Complete CRUD operations for user management
- **PostgreSQL Integration**: Robust database integration with SQLAlchemy ORM
- **Docker Support**: Containerized application for easy deployment and development
- **Automated Testing**: Comprehensive test suite with pytest and coverage reporting
- **CORS Support**: Configured CORS for cross-origin requests
- **Environment Configuration**: Flexible configuration management with Pydantic Settings
- **API Documentation**: Interactive API documentation with Swagger UI
- **CI/CD Pipeline**: Automated testing and deployment with CircleCI
- **Code Coverage**: Track code coverage with Coveralls integration

## 🛠 Tech Stack

### Backend
- **Framework**: FastAPI v0.119.0
- **Language**: Python 3.13+
- **ORM**: SQLAlchemy v2.0.43
- **Database**: PostgreSQL 14
- **Migration Tool**: Alembic v1.17.0
- **Package Manager**: Poetry
- **ASGI Server**: Uvicorn v0.37.0

### Testing & Quality
- **Testing Framework**: pytest v8.4.2
- **Async Testing**: pytest-asyncio v1.2.0
- **HTTP Client**: httpx v0.28.1
- **Coverage**: pytest-cov v7.0.0
- **CI/CD**: CircleCI
- **Coverage Tracking**: Coveralls

### DevOps
- **Containerization**: Docker & Docker Compose
- **Database**: PostgreSQL 14
- **Environment Management**: python-dotenv, pydantic-settings

## 🏗 Architecture

This project follows **Clean Architecture** principles, ensuring:

- **Separation of Concerns**: Clear boundaries between business logic, data access, and API layers
- **Dependency Inversion**: High-level modules don't depend on low-level modules
- **Testability**: Easy to test with dependency injection and mocking
- **Maintainability**: Well-organized code structure for long-term maintenance

### Architecture Layers

1. **Domain Layer** (`app/modules/*/models.py`): Core business entities and models
2. **Repository Layer** (`app/modules/*/repository.py`): Data access abstraction
3. **Service Layer** (`app/modules/*/service.py`): Business logic and use cases
4. **API Layer** (`app/modules/*/router.py`): HTTP endpoints and request/response handling
5. **Schemas Layer** (`app/modules/*/schemas.py`): Pydantic models for validation and serialization

## 📁 Project Structure

```
Challenge/
├── backend/
│   ├── alembic/                 # Database migrations
│   │   ├── versions/            # Migration files
│   │   └── env.py               # Alembic environment configuration
│   ├── app/
│   │   ├── core/                # Core application components
│   │   │   ├── base.py          # Base database model
│   │   │   ├── config.py        # Application configuration
│   │   │   ├── cors.py          # CORS configuration
│   │   │   ├── databse.py       # Database connection
│   │   │   └── clients.py       # External API clients
│   │   └── modules/             # Feature modules
│   │       ├── user/            # User management module
│   │       │   ├── models.py    # User database models
│   │       │   ├── repository.py # User data access
│   │       │   ├── service.py   # User business logic
│   │       │   ├── router.py    # User API endpoints
│   │       │   └── schemas.py   # User Pydantic schemas
│   │       ├── pokemon/         # Pokemon module
│   │       └── auth/            # Authentication module
│   ├── tests/                   # Test suites
│   │   ├── conftest.py          # pytest configuration
│   │   └── users/               # User module tests
│   ├── main.py                  # Application entry point
│   ├── pyproject.toml           # Poetry dependencies
│   └── pytest.ini               # pytest configuration
├── .circleci/
│   └── config.yml               # CircleCI configuration
├── docker-compose.yml           # Docker Compose configuration
├── docker-compose.test.yml      # Test environment configuration
└── README.md                    # Project documentation
```

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Docker** (v20.10+) and **Docker Compose** (v2.0+)
- **Python** 3.13 or higher
- **Poetry** (Python package manager)

### Installing Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/FranAlcoba66/fast-api-backend-challenge.git
cd fast-api-backend-challenge
```

### 2. Environment Setup

Create a `.env` file in the `backend` directory:

```env
# Application Configuration
APP_NAME=Challenge
APP_ENV=local
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
PROJECT_NAME=Challenge API
VERSION=0.1.0
API_V1_STR=/api/v1

# Database Configuration
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=challenge
DATABASE_URL=postgresql://user:password@db:5432/challenge

# Security Configuration
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database Connection Pool
DB_POOL_SIZE=5
DB_MAX_OVERFLOW=10
DB_POOL_TIMEOUT=30
DB_POOL_RECYCLE=1800

# External APIs
POKEMON_API_URL=https://pokeapi.co/api/v2
```

### 3. Start the Application

#### Using Docker Compose (Recommended)

```bash
docker-compose up -d
```

This will start:
- **PostgreSQL** database on port `5432`
- **FastAPI** application on port `8000`

#### Verify the Application

```bash
# Check if containers are running
docker-compose ps

# View application logs
docker-compose logs -f api

# Test the health endpoint
curl http://localhost:8000/
```

### 4. Access the Application

- **API Documentation (Swagger UI)**: http://localhost:8000/docs
- **API Documentation (ReDoc)**: http://localhost:8000/redoc
- **API Base URL**: http://localhost:8000/api/v1
- **Health Check**: http://localhost:8000/

## 💻 Development

### Running Locally (without Docker)

1. **Install Dependencies**

```bash
cd backend
poetry install
```

2. **Start PostgreSQL** (using Docker)

```bash
docker-compose up -d db
```

3. **Run Database Migrations**

```bash
cd backend
poetry run alembic upgrade head
```

4. **Start the Development Server**

```bash
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The `--reload` flag enables hot-reload for development.

### Running with Docker (Development)

The Docker setup includes hot-reload by default:

```bash
docker-compose up -d
docker-compose logs -f api
```

## 🧪 Testing

### Running Tests

#### Option 1: Using Docker Compose (Recommended)

```bash
docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit --exit-code-from tests
```

This will:
- Start a PostgreSQL container for testing
- Run pytest inside a container with Poetry
- Generate coverage reports
- Exit with the test result code

#### Option 2: Running Tests Locally

1. **Ensure PostgreSQL is running**

```bash
docker-compose up -d db
```

2. **Set environment variables**

```bash
export DATABASE_URL="postgresql://user:password@localhost:5432/challenge"
```

3. **Run tests**

```bash
cd backend
poetry install
poetry run pytest -vv --disable-warnings
```

### Running Tests with Coverage

```bash
cd backend
poetry run pytest -vv --disable-warnings --cov=app --cov-report=xml --cov-report=term
```

### Test Structure

```
tests/
├── conftest.py              # pytest fixtures and configuration
└── users/                   # User module tests
    ├── test_user_model.py   # User model tests
    ├── test_user_repository.py # User repository tests
    ├── test_user_service.py # User service tests
    └── test_user_router.py  # User API endpoint tests
```

## 🗄 Database Migrations

### Create a New Migration

```bash
cd backend
poetry run alembic revision --autogenerate -m "description of changes"
```

### Apply Migrations

```bash
poetry run alembic upgrade head
```

### Rollback Migrations

```bash
poetry run alembic downgrade -1
```

### View Migration History

```bash
poetry run alembic history
```

## 📚 API Documentation

### Interactive Documentation

Once the application is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### API Endpoints

#### Health Check
- `GET /` - Health check endpoint

#### User Management
- `GET /api/v1/users` - Get all users
- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/{user_id}` - Get user by ID
- `PUT /api/v1/users/{user_id}` - Update user
- `DELETE /api/v1/users/{user_id}` - Delete user

### Example Request

```bash
# Create a user
curl -X POST "http://localhost:8000/api/v1/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com"
  }'

# Get all users
curl -X GET "http://localhost:8000/api/v1/users"

# Get user by ID
curl -X GET "http://localhost:8000/api/v1/users/1"
```

## 🔄 Continuous Integration

### CircleCI Pipeline

The project uses CircleCI for continuous integration with the following workflow:

1. **Build and Test Job**
   - Installs dependencies using Poetry
   - Sets up PostgreSQL database
   - Runs pytest with coverage
   - Uploads coverage reports to Coveralls

### Pipeline Configuration

The CircleCI configuration (`.circleci/config.yml`) includes:

- Python orb for dependency management
- Coveralls orb for coverage reporting
- PostgreSQL service container
- Automated test execution
- Coverage report upload

### Coverage Tracking

Code coverage is tracked using Coveralls:
- Coverage reports are generated during CI runs
- Coverage status is displayed in the README badge
- View detailed coverage reports at: [Coveralls Dashboard](https://coveralls.io/github/FranAlcoba66/fast-api-backend-challenge)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**

```bash
git checkout -b feature/your-feature-name
```

3. **Make your changes**
4. **Run tests**

```bash
poetry run pytest -vv --disable-warnings
```

5. **Commit your changes**

```bash
git commit -m "Add: your feature description"
```

6. **Push to the branch**

```bash
git push origin feature/your-feature-name
```

7. **Create a Pull Request**

### Code Style

- Follow PEP 8 style guidelines
- Use type hints where applicable
- Write comprehensive tests for new features
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

- **FranAlcoba66** - [GitHub Profile](https://github.com/FranAlcoba66)
- **Email**: franciscoadrianalcoba@gmail.com

## 🙏 Acknowledgments

- FastAPI team for the excellent framework
- SQLAlchemy for the powerful ORM
- pytest for the testing framework
- CircleCI for CI/CD platform
- Coveralls for coverage tracking

---

**Note**: This project is a demonstration of clean architecture principles with FastAPI. For production use, ensure proper security configurations, environment variable management, and database backups.
