from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Hexagonal Microservicios"
    description: str = "Usuarios Microservicios"

    app_v1_port: int = 8001

settings = Settings()