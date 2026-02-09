from domain.user import User
from application.ports.user_repository import UserRepository

class UserMemoryRepository(UserRepository):

    def __init__(self):
        self.users: list[User] = []
        self.counter = 1

    def get_all(self) -> list[User]:
        return self.users

    def create(self, user: User) -> User:
        user.idusuario = self.counter
        self.counter += 1
        self.users.append(user)
        return user