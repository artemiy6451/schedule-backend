"""Файл с зависимостями для уровней образования."""
from app.deegre.repository import DeegreRepository
from app.deegre.services import DeegreService


def deegre_service():
    """Создание сервиса DeegreService с репозиторием DeegreRepository."""
    return DeegreService(DeegreRepository)
