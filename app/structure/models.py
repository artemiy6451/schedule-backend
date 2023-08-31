"""Файл с моделями для модуля `strucure`."""

from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base
from app.structure.schemas import StructureSchema


class Structure(Base):
    """Модель структурного подразделения.

    Содержит:
    name: str
    """

    __tablename__ = "structures"

    name: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)

    def to_read_model(self):
        """Конвертирует данные из модель SQLAlchemy в Pydantic схему."""
        return StructureSchema(
            id=self.id,
            name=self.name,
        )
