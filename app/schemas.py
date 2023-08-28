"""Файл со всеми базовыми Pydantic схемами."""
from fastapi.routing import BaseModel


class SuccesAddSchema(BaseModel):
    """Схема успешного добавления элемента в базу данных."""

    id: int = 1


class SuccesGetSchema(BaseModel):
    """Схема успешного получения всех элементов из базы данных."""

    data: list
