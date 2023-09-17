"""Файл с сервисами структурного подразделения."""

from app.database import async_session_maker
from app.exceptions import ItemNotFoundError
from app.repository import AbstractRepository
from app.services import Service
from app.structure.schemas import StructureSchema, StructureSchemaAdd


class StructureService(Service):
    """Класс сервисов для структурного пдразделения."""

    def __init__(self, repository: type[AbstractRepository]) -> None:
        """Метод для иницилизации сервиса."""
        self.repository = repository(async_session_maker)

    async def add(self, structure: StructureSchemaAdd) -> int:
        """Метод для добавления структурного подразделения."""
        structure_dict = structure.model_dump()
        id = await self.repository.add_one(structure_dict)
        return id

    async def get_all(self) -> list[StructureSchema]:
        """Метод для получения всех структурных подразделений."""
        return await self.repository.find_all()

    async def update(
        self, id: int, structure: StructureSchemaAdd
    ) -> list[StructureSchema]:
        """Метод для обновления структурного подразделения."""
        structure_dict = structure.model_dump()
        res = await self.repository.update_one(id=id, data=structure_dict)
        if res == []:
            raise ItemNotFoundError("Item not found.")
        return res

    async def delete(self, id: int) -> int:
        """Метод для удаления структурного подразделения."""
        res: int = await self.repository.delete_one(id=id)
        return res
