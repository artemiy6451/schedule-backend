"""Файл со схемами для модуля `structure`."""

from pydantic import BaseModel, ConfigDict


class StructureSchema(BaseModel):
    """Схема для показа."""

    id: int
    name: str = "Структурное подразделение."
    model_config = ConfigDict(from_attributes=True)


class StructureSchemaAdd(BaseModel):
    """Схема для добавления в базу данных."""

    name: str
