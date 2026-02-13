from domain.pedido import Pedido
from application.ports.pedido_repository import PedidoRepository

class PedidoMemoryRepository(PedidoRepository):

    def __init__(self):
        self.pedidos: list[Pedido] = []
        self.counter = 1

    def get_all(self) -> list[Pedido]:
        return self.pedidos

    def create(self, pedido: Pedido) -> Pedido:
        pedido.idpedido = self.counter
        self.counter += 1
        self.pedidos.append(pedido)
        return pedido

    def update_pedido(self, pedido_id: int, pedido: Pedido) -> Pedido:
        for p in self.pedidos:
            if p.idpedido == pedido_id:
                p.nombre = pedido.nombre
                p.cantidad = pedido.cantidad
                return p
        return {"message": "Pedido no encontrado"}

    def delete_pedido(self, pedido_id: int):
        for p in self.pedidos:
            if p.idpedido == pedido_id:
                self.pedidos.remove(p)
                return {"message": "Pedido eliminado"}
        return {"message": "Pedido no encontrado"}