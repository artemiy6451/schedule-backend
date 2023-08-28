"""Файл с сервисами для модуля уровня образования."""

from app.deegre.schemas import DeegreSchemaAdd
from app.repository import AbstractRepository
from app.services import Service


class DeegreService(Service):
    """Класс сервиса уровня образования."""

    def __init__(self, repository: type[AbstractRepository]):
        """Инициализация класса с репозиторием `repository`."""
        self.repository: AbstractRepository = repository()

    async def add(self, deegre: DeegreSchemaAdd):
        """Добавление нового уровня образования."""
        deegre_dict = deegre.model_dump()
        id = await self.repository.add_one(deegre_dict)
        return id

    async def get_all(self):
        """Получение всех уровней образования."""
        res = await self.repository.find_all()
        return res

    async def update(self, id: int, deegre: DeegreSchemaAdd):
        """Обновление уровня образования."""
        deegre_dict = deegre.model_dump()
        res = await self.repository.update_one(id=id, data=deegre_dict)
        return res

    async def delete(self, id: int):
        """Удаление уровня образования."""
        res = await self.repository.delete_one(id=id)
        return res
