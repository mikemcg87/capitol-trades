"""Database configuration and session management."""

from typing import AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

# SQLAlchemy Base
Base = declarative_base()

# Synchronous engine for migrations
sync_engine = create_engine(
    settings.database_url_str,
    echo=settings.debug,
    pool_pre_ping=True,
)

# Synchronous session factory
SyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=sync_engine,
)

# Async engine for FastAPI
async_engine = create_async_engine(
    settings.database_url_str.replace("postgresql://", "postgresql+asyncpg://"),
    echo=settings.debug,
    pool_pre_ping=True,
)

# Async session factory
AsyncSessionLocal = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


def get_sync_db() -> Session:
    """Get synchronous database session (for Celery workers)."""
    db = SyncSessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """Get async database session (for FastAPI)."""
    async with AsyncSessionLocal() as session:
        yield session


def create_tables() -> None:
    """Create all tables in the database."""
    Base.metadata.create_all(bind=sync_engine)


def drop_tables() -> None:
    """Drop all tables in the database (use with caution!)."""
    Base.metadata.drop_all(bind=sync_engine)
