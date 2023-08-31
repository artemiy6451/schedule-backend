"""Файл для тестирования модуля `deegre`."""

from fastapi import status
from httpx import AsyncClient
from sqlalchemy import insert, select

from app.database import async_session_maker
from app.deegre.models import Deegre
from app.deegre.schemas import DeegreSchema


class TestDeegreEndpoint:
    """Класс для тестирования работы эндпоинта."""

    async def test_add_deegre_endpoint(self, async_client: AsyncClient):
        """Функция для тестирования работы эндпоинта добавления уровня образования."""
        response = await async_client.post(
            "/deegre",
            json={
                "name": "deegre",
            },
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["id"] == 1

    async def test_get_deegre_endpoint(self, async_client: AsyncClient):
        """Функция для тестирования работы эндпоинта получения уровней образования."""
        response = await async_client.get("/deegre")

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["data"][0]["id"] == 1
        assert response.json()["data"][0]["name"] == "deegre"

    async def test_update_deegre_endpoint(self, async_client: AsyncClient):
        """Функция для тестирования работы эндпоинта обновления уровня образования."""
        response = await async_client.put(
            "/deegre/1",
            json={
                "name": "new deegre",
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["data"][0]["id"] == 1
        assert response.json()["data"][0]["name"] == "new deegre"

    async def test_delete_deegre_endpoint(self, async_client: AsyncClient):
        """Функция для тестирования работы эндпоинта удаления уровня образования."""
        response = await async_client.delete("/deegre/1")

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["id"] == 1


class TestDeegreDataBase:
    """Класс для тестирования базы данных."""

    async def test_create_deegre(self):
        """Функция для тестирования добаления уровня образования в базу данных."""
        async with async_session_maker() as session:
            stmt = insert(Deegre).values(name="Бакалавр")
            await session.execute(stmt)
            await session.commit()

    async def test_get_all_deegre(self):
        """Функция для тестирования получения уровня образования из базы данных."""
        async with async_session_maker() as session:
            query = select(Deegre)
            result = await session.execute(query)
            result = [row[0].to_read_model() for row in result.all()]

            assert result == [
                DeegreSchema(id=1, name="Бакалавр")
            ], "Не соответвие базы данных и итоговых значений."
            print("inside context manager")
        print("outside context manager")
