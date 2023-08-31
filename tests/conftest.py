"""Файл с базовой настройкой pytest."""

import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine

from app.config import settings
from app.database import async_session_maker, get_async_session
from app.main import app
from app.models import Base

DATABASE_URL = f"postgresql+asyncpg://{settings.test_db_user}:{settings.test_db_pass}@\
{settings.test_db_host}:{settings.test_db_port}/{settings.test_db_name}"


engine_test = create_async_engine(DATABASE_URL)
async_session_maker.configure(bind=engine_test)


async def override_get_async_session():
    """Функция возвращающая сессию подключения к базе данных."""
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(autouse=True, scope="class")
async def prepare_database():
    """Подготовка базы данных к тестам."""
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    """Созднание асинхронного клиента для тестирования."""
    async with AsyncClient(app=app, base_url="http://localhost:8000") as async_client:
        yield async_client


@pytest.fixture(scope="session")
def event_loop():
    """Создание event loop'a."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()
