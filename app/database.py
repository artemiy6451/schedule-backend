"""Database default settings and session function for connection."""

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings


class Base(DeclarativeBase):
    """Base class for alembic migration."""

    pass


database_uri = f"postgresql+asyncpg://{settings.db_user}:{settings.db_pass}@\
                {settings.db_host}:{settings.db_port}/{settings.db_name}?\
                async_fallback=True"


engine = create_async_engine(database_uri)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    """Return database connection session."""
    async with async_session_maker() as session:
        yield session
