"""Application configuration using Pydantic settings."""

from typing import Literal

from pydantic import Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Application
    app_name: str = Field(default="capitol-trades", description="Application name")
    env: Literal["development", "staging", "production"] = Field(
        default="development", description="Environment"
    )
    debug: bool = Field(default=True, description="Debug mode")

    # API
    api_host: str = Field(default="0.0.0.0", description="API host")
    api_port: int = Field(default=8000, description="API port")
    api_reload: bool = Field(default=True, description="API auto-reload")

    # Database
    database_url: PostgresDsn = Field(
        description="PostgreSQL database URL",
    )

    # Redis
    redis_url: RedisDsn = Field(
        description="Redis URL",
    )

    # Celery
    celery_broker_url: RedisDsn = Field(
        description="Celery broker URL",
    )
    celery_result_backend: RedisDsn = Field(
        description="Celery result backend URL",
    )

    # Bright Data
    bright_data_api_key: str = Field(
        description="Bright Data API key",
    )
    bright_data_zone: str = Field(
        default="residential",
        description="Bright Data zone name",
    )

    # Logging
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO",
        description="Logging level",
    )

    @property
    def database_url_str(self) -> str:
        """Return database URL as string."""
        return str(self.database_url)

    @property
    def redis_url_str(self) -> str:
        """Return Redis URL as string."""
        return str(self.redis_url)


# Global settings instance
settings = Settings()
