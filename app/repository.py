"""Файл с базовыми репозиториями для работы с базой данных.

Здесь аккумулирована вся работа с базой данных.
"""

from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.models import Base


class AbstractRepository(ABC):
    """Абстрактрный класс Репозиторий.

    Содержит базовые методы для работы с базой данных.
    """

    @abstractmethod
    def __init__(self, session):
        """Метод для инициализации репозитория.

        И указания сессии подключения к базе данных.
        """
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, id: int) -> list:
        """Метод для получения одного элемента из базы данных."""
        raise NotImplementedError

    @abstractmethod
    async def find_all(self) -> list:
        """Метод для получения нескольких элементов из базы данных."""
        raise NotImplementedError

    @abstractmethod
    async def add_one(self, data: dict) -> int:
        """Метод для вставки одного элемента в базу данных."""
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, id: int, data: dict):
        """Метод для обновления одного элемента в базе данных."""
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, id: int):
        """Метод для удаления одного элемента из базы данных."""
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    """Репозиторий для работы с SQLAlchemy."""

    model: Type[Base]

    def __init__(self, session: async_sessionmaker[AsyncSession]):
        """Метод для инициализации репозитория."""
        self.session: AsyncSession = session()

    async def find_one(self, id: int) -> list:
        """Метод для поиска в базе данных элемента модели `model`."""
        stmt = select(self.model).filter_by(id=id)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def find_all(self) -> list:
        """Метод для поиска в базе данных элементов модели `model`."""
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def add_one(self, data: dict) -> int:
        """Добавление одного элемента модели `model` с данными `data`."""
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()

    async def update_one(self, id: int, data: dict) -> list:
        """Обновление одного элемента с id `id`."""
        stmt = (
            update(self.model)
            .values(**data)
            .where(self.model.id == id)
            .returning(self.model)
        )
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        await self.session.commit()
        return res

    async def delete_one(self, id: int):
        """Удалние одного эелемента с id `id`."""
        stmt = delete(self.model).where(self.model.id == id).returning(self.model.id)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()
