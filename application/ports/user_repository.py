from abc import ABC, abstractmethod
from domain.user import User

class UserRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    def update_user(self, user_id: int, user: User) -> User:
        pass

    def delete_user(self, user_id: int):
        pass