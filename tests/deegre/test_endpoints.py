"""Файл для тестирования эндпоинтов модуля `deegre`."""

from fastapi import status
from httpx import AsyncClient


class TestDeegreEndpoint:
    """Класс для тестирования работы эндпоинтов."""

    async def test_add_deegre_endpoint(self, async_client: AsyncClient):
        """Функция для тестирования работы эндпоинта добавления уровня образования."""
        payload = {
            "name": "deegre",
        }

        response = await async_client.post("/deegre", json=payload)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["id"] == 1

        response = await async_client.post("/deegre", json=payload)

        assert response.status_code == status.HTTP_409_CONFLICT
        assert response.json()["details"] == "Item already exist."

    async def test_get_deegre_endpoint(self, async_client: AsyncClient):
        """Функция для тестирования работы эндпоинта получения уровней образования."""
        response = await async_client.get("/deegre")

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["data"][0]["id"] == 1
        assert response.json()["data"][0]["name"] == "deegre"

    async def test_update_deegre_endpoint(self, async_client: AsyncClient):
        """Функция для тестирования работы эндпоинта обновления уровня образования."""
        payload = {
            "name": "new deegre",
        }

        response = await async_client.put("/deegre/1", json=payload)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["data"][0]["id"] == 1
        assert response.json()["data"][0]["name"] == "new deegre"

        response = await async_client.put("/deegre/1", json=payload)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["data"][0]["id"] == 1
        assert response.json()["data"][0]["name"] == "new deegre"

    async def test_delete_deegre_endpoint(self, async_client: AsyncClient):
        """Функция для тестирования работы эндпоинта удаления уровня образования."""
        response = await async_client.delete("/deegre/1")

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["id"] == 1

        response = await async_client.delete("/deegre/1")
        assert response.status_code == status.HTTP_409_CONFLICT
        assert response.json()["details"] == "Item not found."
