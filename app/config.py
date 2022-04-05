import os
from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Configs"""

    # General
    APP_NAME: str = "Quickrun FastAPI"
    PROJECT_DIR: str = os.path.dirname(__file__)
    DEBUG: bool = False

    # Database
    DB_TYPE: str = "sqlite"
    DB_USER: str = ""
    DB_PASSWORD: str = ""
    DB_HOST: str = ""
    DB_PORT: int = 0
    DB_NAME: str = "db"

    # Auth
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SECRET_KEY: str = "secret"
    ALGORITHM: str = "HS256"

    # CORS authorizations
    CORS_ALLOW_ORIGINS: List[str] = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ["*"]
    CORS_ALLOW_HEADERS: List[str] = ["*"]


settings = Settings()
