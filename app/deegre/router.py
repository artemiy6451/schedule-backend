"""Файл с эндпоинтами для уровней образования."""
from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.deegre.dependencies import deegre_service
from app.deegre.repository import DeegreRepository
from app.deegre.schemas import DeegreSchemaAdd
from app.deegre.services import DeegreService
from app.schemas import SuccesAddSchema, SuccesGetSchema

router = APIRouter(prefix="/deegre", tags=["Deegre"])


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": SuccesAddSchema},
    },
)
async def add_deegre(
    deegre: DeegreSchemaAdd, service: Annotated[DeegreService, Depends(deegre_service)]
):
    """Эндпоинт для добавления уровня образования в базу данных."""
    id = await service.add(deegre)
    return {"id": id}


@router.get("", responses={status.HTTP_200_OK: {"model": SuccesGetSchema}})
async def get_all_deegre():
    """Получение всех уровней образования."""
    res = await DeegreRepository().find_all()
    return SuccesGetSchema(data=res)
