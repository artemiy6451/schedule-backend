"""Файл со схемами для модуля `direction`."""


from pydantic import BaseModel, ConfigDict

from app.schemas import SuccesGetSchema


class DirectionSchema(BaseModel):
    """Главная схема модуля `direction`."""

    id: int
    name: str = "Направление подготовки."

    model_config = ConfigDict(from_attributes=True)


class DirectionSchemaAdd(BaseModel):
    """Схема для добаления нового направления подготовки."""

    name: str = "Направлние поготовки."
    structure_id: int = 1


class DirectionSchemaGet(SuccesGetSchema):
    """Схема для отображения направления подготовки."""

    data: list[DirectionSchema]
