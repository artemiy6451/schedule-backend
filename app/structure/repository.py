"""Файл с резозиториями для структурного подразделения."""

from app.repository import SQLAlchemyRepository
from app.structure.models import Structure


class StructureRepository(SQLAlchemyRepository):
    """Репозиторий для структурного подразделения."""

    model = Structure
