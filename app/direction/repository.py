"""Файл с репозиториями для модуля `direction`."""


from app.direction.models import Direction
from app.repository import SQLAlchemyRepository


class DirectionRepository(SQLAlchemyRepository):
    """Репозиторий направления подготовки."""

    model = Direction
