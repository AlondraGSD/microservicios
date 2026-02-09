from domain.user import User
from application.ports.user_repository import UserRepository

class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_users(self):
        return self.repository.get_all()

    def create_user(self, user: User):
        return self.repository.create(user)