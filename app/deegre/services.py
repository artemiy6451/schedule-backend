"""Файл с сервисами для модуля уровня образования."""

from sqlalchemy.exc import IntegrityError, NoResultFound

from app.database import async_session_maker
from app.deegre.schemas import DeegreSchema, DeegreSchemaAdd
from app.exceptions import ItemAlreadyExistError, ItemNotFoundError, UniversalError
from app.repository import AbstractRepository
from app.services import Service


class DeegreService(Service):
    """Класс сервиса уровня образования."""

    def __init__(self, repository: type[AbstractRepository]):
        """Инициализация класса с репозиторием `repository`."""
        self.repository: AbstractRepository = repository(async_session_maker)

    async def add(self, deegre: DeegreSchemaAdd) -> int:
        """Добавление нового уровня образования."""
        try:
            deegre_dict = deegre.model_dump()
            id = await self.repository.add_one(deegre_dict)
            return id
        except IntegrityError as e:
            if "UniqueViolationError" in e.orig.__str__():
                raise ItemAlreadyExistError("Item already exist.") from None
            raise UniversalError(e) from e
        except Exception as e:
            raise UniversalError(e) from e

    async def get_all(self) -> list[DeegreSchema]:
        """Получение всех уровней образования."""
        res: list[DeegreSchema] = await self.repository.find_all()
        return res

    async def update(self, id: int, deegre: DeegreSchemaAdd) -> list[DeegreSchema]:
        """Обновление уровня образования."""
        deegre_dict = deegre.model_dump()
        res: list[DeegreSchema] = await self.repository.update_one(
            id=id, data=deegre_dict
        )
        if res == []:
            raise ItemNotFoundError("Item not found.")
        return res

    async def delete(self, id: int) -> int:
        """Удаление уровня образования."""
        try:
            res: int = await self.repository.delete_one(id=id)
            return res
        except NoResultFound:
            raise ItemNotFoundError("Item not found.") from NoResultFound
        except Exception:
            raise UniversalError from Exception
