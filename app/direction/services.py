"""Файл с сервисами для модуля `direction`."""


from sqlalchemy.exc import IntegrityError, NoResultFound

from app.database import async_session_maker
from app.direction.schemas import DirectionSchema, DirectionSchemaAdd
from app.exceptions import ItemAlreadyExistError, ItemNotFoundError, UniversalError
from app.repository import AbstractRepository
from app.services import Service


class DirectionService(Service):
    """Класс сервиса для направления подготовки."""

    def __init__(self, repository: type[AbstractRepository]):
        """Инициализация класса с репозиторием `repository`."""
        self.repository: AbstractRepository = repository(async_session_maker)

    async def add(self, direction: DirectionSchemaAdd) -> int:
        """Добавление нового направления подготовки."""
        try:
            direction_dict = direction.model_dump()
            id = await self.repository.add_one(direction_dict)
            return id
        except IntegrityError as e:
            if "UniqueViolationError" in e.orig.__str__():
                raise ItemAlreadyExistError("Item already exist.") from None
            raise UniversalError(e) from e
        except Exception as e:
            raise UniversalError(e) from e

    async def get_all(self) -> list[DirectionSchema]:
        """Получение всех уровней образования."""
        res: list[DirectionSchema] = await self.repository.find_all()
        return res

    async def update(
        self, id: int, direction: DirectionSchemaAdd
    ) -> list[DirectionSchema]:
        """Обновление направления подготовки."""
        direction_dict = direction.model_dump()
        res: list[DirectionSchema] = await self.repository.update_one(
            id=id, data=direction_dict
        )
        if res == []:
            raise ItemNotFoundError("Item not found.")
        return res

    async def delete(self, id: int) -> int:
        """Удаление напрвеления подготовки."""
        try:
            res: int = await self.repository.delete_one(id=id)
            return res
        except NoResultFound:
            raise ItemNotFoundError("Item not found.") from NoResultFound
        except Exception:
            raise UniversalError from Exception
