"""Файл для тестирования работы базы данных с модулем `deegre`."""

from sqlalchemy import insert, select

from app.database import async_session_maker
from app.deegre.models import Deegre
from app.deegre.schemas import DeegreSchema


class TestDeegreDataBase:
    """Класс для тестирования базы данных."""

    async def test_create_deegre(self):
        """Функция для тестирования добаления уровня образования в базу данных."""
        deegre: DeegreSchema = DeegreSchema(id=1, name="Бакалавр")

        async with async_session_maker() as session:
            stmt = insert(Deegre).values(deegre.model_dump())
            await session.execute(stmt)
            await session.commit()

            query = select(Deegre).filter_by(id=deegre.id)
            result = await session.execute(query)
            result = [row[0].to_read_model() for row in result.all()]
            assert result == [
                deegre
            ], "Как то не так добавились значения в базу данных."

    async def test_get_all_deegre(self):
        """Функция для тестирования получения уровня образования из базы данных."""
        deegre: DeegreSchema = DeegreSchema(id=1, name="Бакалавр")

        async with async_session_maker() as session:
            query = select(Deegre)
            result = await session.execute(query)
            result = [row[0].to_read_model() for row in result.all()]

            assert result == [deegre], "Не соответвие базы данных и итоговых значений."
