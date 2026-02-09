from fastapi import FastAPI
from domain.user import User
from application.services.user_service import UserService
from infrastructure.adapters.user_memory_repository import UserMemoryRepository
from core.config import settings

app = FastAPI(
    title=settings.app_name,
    description=settings.description
)

repository = UserMemoryRepository()
service = UserService(repository)

@app.get("/users")
def get_users():
    return service.get_users()

@app.post("/users")
def create_user(user: User):
    return service.create_user(user)