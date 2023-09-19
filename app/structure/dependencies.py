"""Файл с зависимостями для структурного подразделения."""

from app.structure.repository import StructureRepository
from app.structure.services import StructureService


def structure_service():
    """Фунция для инизиализации сервисов для структурного подразделения."""
    return StructureService(StructureRepository)
