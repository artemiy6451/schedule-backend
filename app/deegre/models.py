"""Файл модуля уровня образования для описания моделей sqlalchemy."""

from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from app.deegre.schemas import DeegreSchema
from app.models import Base


class Deegre(Base):
    """Модель уровня образования.

    Содержит:
    name: str
    """

    __tablename__ = "deegres"

    name: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)

    def to_read_model(self):
        """Конвертирует данные из модель SQLAlchemy в Pydantic схему."""
        return DeegreSchema(
            id=self.id,
            name=self.name,
        )
