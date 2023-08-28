"""Файл с Pydantic схемами."""
from fastapi.routing import BaseModel


class DeegreSchema(BaseModel):
    """Схема для отображения модели."""

    id: int
    name: str

    class Config:
        """Метакласс для кофигурации схемы."""

        from_attributes = True


class DeegreSchemaAdd(BaseModel):
    """Схема для добавления модели."""

    name: str
