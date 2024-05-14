# FastAPI Project

## Description

This project is a [FastAPI](https://fastapi.tiangolo.com/) application that serves as a backend API for a web application. It provides various endpoints for user authentication, budget management, expense tracking, peer-to-peer lending, payments, notifications, and more.

## Features

- User Authentication: Endpoints for user registration, login, and profile management.
- Budget Management: CRUD operations for budget categories and expenses.
- Expense Tracking: Endpoints for managing user expenses and categories.
- Peer-to-Peer Lending: Functionality for requesting, accepting, and rejecting loans.
- Payments: Endpoints for sending payments, canceling payments, and viewing payment details.
- Notifications: API endpoints for managing user notifications.
- Dashboard: Overview data for user dashboards.

## Technologies Used

- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **PostgreSQL**: A powerful, open-source relational database.
- **SQLAlchemy**: An ORM (Object-Relational Mapping) library for database interactions.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **JWT (JSON Web Tokens)**: Token-based authentication for securing API endpoints.
- **Docker**: Containerization for easy deployment and scaling.
- **GitHub Actions**: Continuous Integration/Continuous Deployment (CI/CD) for automated testing and deployment.
- **pytest**: Testing framework for unit and integration tests.
- **Faker**: Library for generating fake data for testing and seeding.

## Getting Started

### Prerequisites

- Python 3.x
- Docker (optional)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/isaacoduh/budfi-backend-v1.git
```
2. Install Dependencies

```bash
cd budfi-clone
pip install -r requirements.txt
```
3. Setup Environment File

4. Run the application
```commandline
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
5. Docker
```commandline
docker-compose up -d
```

### Usage
- Access the API documentation and interact with the endpoints using the Swagger uI at `http://localhost:8000/docs` or the ReDoc UI at `http://localhost:8000/redoc`.
- Use API endpoints to perform various operations such as user authentication, budget management, expense tracking etc.

### Testing
```bash
pytest
```