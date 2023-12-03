"""Файл с моделями для модуля `direction`."""


from sqlalchemy import VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base
from app.structure.models import Structure


class Direction(Base):
    """Модель направления подготовки.

    Содержит:
    name: str
    structure_id: int
    """

    __tablename__ = "direction"

    name: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, unique=True)
    structure_id: Mapped[int] = mapped_column(ForeignKey(Structure.id))
