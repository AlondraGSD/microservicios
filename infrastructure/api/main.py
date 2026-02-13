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

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return service.update_user(user_id, user)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return service.delete_user(user_id)