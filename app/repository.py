"""Файл с базовыми репозиториями для работы с базой данных.

Здесь аккумулирована вся работа с базой данных.
"""

from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy import delete, insert, select, update

from app.database import async_session_maker
from app.models import Base


class AbstractRepository(ABC):
    """Абстрактрный класс Репозиторий.

    Содержит базовые методы для работы с базой данных.
    """

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

    async def find_one(self, id: int) -> list:
        """Метод для поиска в базе данных элемента модели `model`."""
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(id=id)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    async def find_all(self) -> list:
        """Метод для поиска в базе данных элементов модели `model`."""
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    async def add_one(self, data: dict) -> int:
        """Добавление одного элемента модели `model` с данными `data`."""
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def update_one(self, id: int, data: dict) -> list:
        """Обновление одного элемента с id `id`."""
        async with async_session_maker() as session:
            stmt = (
                update(self.model)
                .values(**data)
                .where(self.model.id == id)
                .returning(self.model)
            )
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            await session.commit()
            return res

    async def delete_one(self, id: int):
        """Удалние одного эелемента с id `id`."""
        async with async_session_maker() as session:
            stmt = (
                delete(self.model).where(self.model.id == id).returning(self.model.id)
            )
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
