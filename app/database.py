"""Файл с базовой настройкой и подключением к базе данных."""

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import settings

DATABASE_URL = (
    f"postgresql+asyncpg://{settings.db_user}:{settings.db_pass}@"
    f"{settings.db_host}:{settings.db_port}/{settings.db_name}"
)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    """Return database connection session."""
    async with async_session_maker() as session:
        yield session
