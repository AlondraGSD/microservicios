from pydantic import BaseModel
from typing import Optional

class Pedido(BaseModel):
    idpedido: Optional[int] = None
    nombre: str
    cantidad: int