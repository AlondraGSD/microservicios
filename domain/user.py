from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    idusuario: Optional[int] = None
    nombre: str
    email: EmailStr