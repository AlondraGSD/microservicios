from fastapi import FastAPI
from domain.pedido import Pedido
from application.services.pedido_service import PedidoService
from infrastructure.adapters.pedido_memory_repository import PedidoMemoryRepository
from core.config import settings

app = FastAPI(
    title=settings.app_name,
    description=settings.description
)

repository = PedidoMemoryRepository()
service = PedidoService(repository)

@app.get("/pedidos")
def get_pedidos():
    return service.get_pedidos()

@app.post("/pedidos")
def create_pedido(pedido: Pedido):
    return service.create_pedido(pedido)

@app.put("/pedidos/{pedido_id}")
def update_pedido(pedido_id: int, pedido: Pedido):
    return service.update_pedido(pedido_id, pedido)

@app.delete("/pedidos/{pedido_id}")
def delete_pedido(pedido_id: int):
    return service.delete_pedido(pedido_id)