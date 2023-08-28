"""Файл со всеми базовыми Pydantic схемами."""
from pydantic import BaseModel


class SuccesAddSchema(BaseModel):
    """Схема успешного добавления элемента в базу данных."""

    id: int = 1


class SuccesGetSchema(BaseModel):
    """Схема успешного получения всех элементов из базы данных."""

    data: list


class SuccesDeleteSchema(SuccesAddSchema):
    """Схема успешного удаления элеметна из базы данных."""

    pass
