from domain.pedido import Pedido
from application.ports.pedido_repository import PedidoRepository

class PedidoService:

    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    def get_pedidos(self):
        return self.repository.get_all()

    def create_pedido(self, pedido: Pedido):
        return self.repository.create(pedido)

    def update_pedido(self, pedido_id: int, pedido: Pedido):
        return self.repository.update_pedido(pedido_id, pedido)

    def delete_pedido(self, pedido_id: int):
        return self.repository.delete_pedido(pedido_id)