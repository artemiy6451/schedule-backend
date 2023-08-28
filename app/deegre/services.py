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
