"""Файл с базовыми сервисами."""
from abc import ABC, abstractmethod


class Service(ABC):
    """Абстрактный класс сервиса."""

    @abstractmethod
    async def add():
        """Абстрактный метод для добавления элемента в базу данных."""
        raise NotImplementedError

    @abstractmethod
    async def get_all():
        """Абстрактный метод получения всех элементов из базы данных."""
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: int):
        """Абстрактный метод для обновления одного элемента в базе данных."""
        raise NotImplementedError
