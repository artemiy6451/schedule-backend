"""Файл с базовыми сервисами."""
from abc import ABC, abstractmethod


class Service(ABC):
    """Абстрактный класс сервиса."""

    @abstractmethod
    def add():
        """Абстрактный метод для добавления элемента в базу данных."""
        raise NotImplementedError
