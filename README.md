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

## Prerequisites

- Docker and Docker Compose
- Python 3.13 or higher
- Poetry (Python package manager)

## Getting Started

1. **Clone the repository**

```bash
git clone <repository-url>
cd Challenge
```

2. **Environment Setup**

Create a `.env` file in the `backend` directory with the following variables:

```env
DATABASE_URL=postgresql://user:password@db:5432/challenge
```

3. **Start the Application**

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

```bash
docker-compose --profile testing up -d test_db
poetry run pytest
```

### Database Migrations

```bash
# Generate a new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head
```

## API Endpoints

- `GET /`: Health check endpoint
- `GET /api/v1/users`: User-related endpoints

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
