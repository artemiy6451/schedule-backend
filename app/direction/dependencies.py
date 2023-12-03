"""Файл с зависимостями для модуля `direction`."""

from app.direction.repository import DirectionRepository
from app.direction.services import DirectionService


def direction_service():
    """Создание сервиса DirectionService с репозиторием DirectionRepository."""
    return DirectionService(DirectionRepository)
