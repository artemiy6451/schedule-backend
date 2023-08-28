"""Файл с эндпоинтами для уровней образования."""
from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.deegre.dependencies import deegre_service
from app.deegre.schemas import DeegreSchemaAdd, DeegreSchemaGet
from app.deegre.services import DeegreService
from app.schemas import SuccesAddSchema, SuccesDeleteSchema

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
    return SuccesAddSchema(id=id)


@router.get("", responses={status.HTTP_200_OK: {"model": DeegreSchemaGet}})
async def get_all_deegre(service: Annotated[DeegreService, Depends(deegre_service)]):
    """Эндпоинт для получения всех уровней образования."""
    res = await service.get_all()
    return DeegreSchemaGet(data=res)


@router.put("/{id}", responses={status.HTTP_200_OK: {"model": DeegreSchemaGet}})
async def update_one_deegre(
    id: int,
    deegre: DeegreSchemaAdd,
    service: Annotated[DeegreService, Depends(deegre_service)],
):
    """Эндпоинт для обновления уровня образовния."""
    res = await service.update(id, deegre)
    return DeegreSchemaGet(data=res)


@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": SuccesDeleteSchema}})
async def delete_one_deegre(
    id: int, service: Annotated[DeegreService, Depends(deegre_service)]
):
    """Эндпоинт для удаления уровня образования."""
    id = await service.delete(id)
    return SuccesDeleteSchema(id=id)
