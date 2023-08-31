"""Файл с репозиторием Deegre для работы с базой данных."""
from app.deegre.models import Deegre
from app.repository import SQLAlchemyRepository


class DeegreRepository(SQLAlchemyRepository):
    """Репозиторий для работы с deegre(уровнем образования)."""

    model = Deegre
