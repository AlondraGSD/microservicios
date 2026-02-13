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

    def update_user(self, user_id: int, user: User) -> User:
        for u in self.users:
            if u.idusuario == user_id:
                u.nombre = user.nombre
                u.email = user.email
                return u
        return {"message": "Usuario no encontrado"}

    def delete_user(self, user_id: int):
        for u in self.users:
            if u.idusuario == user_id:
                self.users.remove(u)
                return {"message": "Usuario eliminado"}
        return {"message": "Usuario no encontrado"}