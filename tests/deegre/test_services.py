"""Файл для тестирования сервисов модуля `deegre`."""

import pytest

from app.deegre.repository import DeegreRepository
from app.deegre.schemas import DeegreSchema, DeegreSchemaAdd
from app.deegre.services import DeegreService
from app.exceptions import ItemAlreadyExistError, ItemNotFoundError
from app.schemas import ItemAlreadyExistSchema, ItemNotFoundSchema


class TestDeegreServices:
    """Класс для тестирования работы сервисов уровня образования."""

    async def test_add(self):
        """Метод для тестирования работы добавления уровня образования."""
        deegre = DeegreSchemaAdd(name="Бакалавр")

        id = await DeegreService(DeegreRepository).add(deegre)
        assert id == 1

        with pytest.raises(ItemAlreadyExistError) as excinfo:
            await DeegreService(DeegreRepository).add(deegre)
        assert str(excinfo.value) == ItemAlreadyExistSchema().details

        deegre = DeegreSchemaAdd(name="Аспирантура")
        id = await DeegreService(DeegreRepository).add(deegre)
        assert id == 3

    async def test_get_all(self):
        """Метод для тестирования получения всех уровней образования."""
        deegres: list[DeegreSchema] = await DeegreService(DeegreRepository).get_all()

        assert deegres == [
            DeegreSchema(id=1, name="Бакалавр"),
            DeegreSchema(id=3, name="Аспирантура"),
        ]

    async def test_update(self):
        """Метод для тестирования обновления уровня расписания."""
        deegre: DeegreSchemaAdd = DeegreSchemaAdd(name="Новый бакалавриат")

        deegres: list[DeegreSchema] = await DeegreService(DeegreRepository).update(
            id=1, deegre=deegre
        )

        assert deegres == [DeegreSchema(id=1, name="Новый бакалавриат")]

        with pytest.raises(ItemNotFoundError) as excinfo:
            await DeegreService(DeegreRepository).update(id=10, deegre=deegre)

        assert str(excinfo.value) == ItemNotFoundSchema().details

    async def test_delete(self):
        """Метод для тестирования удаления уровня образования."""
        id: int = await DeegreService(DeegreRepository).delete(id=1)

        assert id == 1

        with pytest.raises(ItemNotFoundError) as excinfo:
            await DeegreService(DeegreRepository).delete(id=1)

        assert str(excinfo.value) == ItemNotFoundSchema().details
