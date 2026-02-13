from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Hexagonal Microservicios"
    description: str = "CRUD de Usuarios/Pedidos Microservicios"

    app_v1_port: int = 8001
    app_v2_port: int = 8002

settings = Settings()