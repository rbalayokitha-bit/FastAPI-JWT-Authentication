# FastAPI JWT Authentication

A secure User Management REST API built using FastAPI, Python, SQLAlchemy, SQLite and JWT Authentication.

## Features

- User Registration
- User Login
- Password Hashing using bcrypt
- JWT Token Authentication
- Get Current User
- Update User Details
- Delete User
- SQLite Database
- Interactive API Documentation

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT
- Pydantic
- bcrypt

## Project Structure

```text
FastAPI-JWT-Authentication/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routes.py
│
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

## API Documentation

Open your browser:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /register | Register a user |
| POST | /login | Login |
| GET | /users/me | Get current user |
| PUT | /users/me | Update user |
| DELETE | /users/me | Delete user |

## Database

SQLite is used to store user information.

Passwords are stored as bcrypt hashes.

## Author

Bala Yokitha
B.Tech Artificial Intelligence and Data Science