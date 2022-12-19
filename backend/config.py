from functools import lru_cache

from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    project_title: str = 'Book Summarizer'
    project_version: str = '0.1.0'
    base_url: str
    database_url: str
    env_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    backend_cors_origins: list[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
