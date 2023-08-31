"""Файл с Pydantic схемами."""
from pydantic import BaseModel, ConfigDict

from app.schemas import SuccesGetSchema


class DeegreSchema(BaseModel):
    """Схема для отображения модели."""

    id: int
    name: str = "Уровень образования"

    model_config = ConfigDict(from_attributes=True)


class DeegreSchemaAdd(BaseModel):
    """Схема для добавления модели."""

    name: str


class DeegreSchemaGet(SuccesGetSchema):
    """Схема для отображения всех уровней образования."""

    data: list[DeegreSchema]
