from abc import ABC, abstractmethod
from domain.pedido import Pedido

class PedidoRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Pedido]:
        pass

    @abstractmethod
    def create(self, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    def update_pedido(self, pedido_id: int, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    def delete_pedido(self, pedido_id: int):
        pass