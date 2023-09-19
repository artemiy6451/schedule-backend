"""Файл со схемами для модуля `structure`."""

from pydantic import BaseModel, ConfigDict

from app.schemas import SuccesGetSchema


class StructureSchema(BaseModel):
    """Схема для показа."""

    id: int
    name: str = "Структурное подразделение."

    model_config = ConfigDict(from_attributes=True)


class StructureSchemaAdd(BaseModel):
    """Схема для добавления структурного подразделения."""

    name: str


class StructureSchemaGet(SuccesGetSchema):
    """Схема для получения списка структурного подразделения."""

    data: list[StructureSchema]
