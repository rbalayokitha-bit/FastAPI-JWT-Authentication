from fastapi import FastAPI

from app.database import engine, Base
from app import models
from app.routes import router

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI application
app = FastAPI(
    title="FastAPI JWT Authentication",
    description="A secure User Management API",
    version="1.0.0"
)

# Connect API routes
app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI JWT Authentication API",
        "status": "Running Successfully"
    }


@app.get("/health")
def health_check():
    return {
        "status": "Healthy",
        "application": "FastAPI"
    }