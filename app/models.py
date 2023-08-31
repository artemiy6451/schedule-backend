"""Файл с базовыми моделями приложения."""
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Базовый класс для всех моделей SQLAlchemy.

    Содержит:
    id: int
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
