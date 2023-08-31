"""Файл с эндпоинтами для уровней образования."""
from typing import Annotated

from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from app.deegre.dependencies import deegre_service
from app.deegre.schemas import DeegreSchemaAdd, DeegreSchemaGet
from app.deegre.services import DeegreService
from app.exceptions import ItemAlreadyExistError, ItemNotFoundError, UniversalError
from app.schemas import (
    ItemAlreadyExistSchema,
    ItemNotFoundSchema,
    SuccesAddSchema,
    SuccesDeleteSchema,
    UniversalErrorSchema,
)

router = APIRouter(prefix="/deegre", tags=["Deegre"])


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": SuccesAddSchema},
        status.HTTP_409_CONFLICT: {"model": ItemAlreadyExistSchema},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": UniversalErrorSchema},
    },
)
async def add_deegre(
    deegre: DeegreSchemaAdd, service: Annotated[DeegreService, Depends(deegre_service)]
):
    """Эндпоинт для добавления уровня образования в базу данных."""
    try:
        id = await service.add(deegre)
        return SuccesAddSchema(id=id)
    except ItemAlreadyExistError:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content=ItemAlreadyExistSchema().model_dump(),
        )
    except UniversalError as e:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content=UniversalErrorSchema(details=e.__str__()).model_dump(),
        )


@router.get("", responses={status.HTTP_200_OK: {"model": DeegreSchemaGet}})
async def get_all_deegre(service: Annotated[DeegreService, Depends(deegre_service)]):
    """Эндпоинт для получения всех уровней образования."""
    res = await service.get_all()
    return DeegreSchemaGet(data=res)


@router.put(
    "/{id}",
    responses={
        status.HTTP_200_OK: {"model": DeegreSchemaGet},
        status.HTTP_409_CONFLICT: {"model": ItemNotFoundSchema},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": UniversalErrorSchema},
    },
)
async def update_one_deegre(
    id: int,
    deegre: DeegreSchemaAdd,
    service: Annotated[DeegreService, Depends(deegre_service)],
):
    """Эндпоинт для обновления уровня образовния."""
    try:
        res = await service.update(id, deegre)
        return DeegreSchemaGet(data=res)
    except ItemNotFoundError:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content=ItemNotFoundSchema().model_dump(),
        )
    except UniversalError as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=UniversalErrorSchema(details=e.__str__()).model_dump(),
        )


@router.delete(
    "/{id}",
    responses={
        status.HTTP_200_OK: {"model": SuccesDeleteSchema},
        status.HTTP_409_CONFLICT: {"model": ItemNotFoundSchema},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": UniversalErrorSchema},
    },
)
async def delete_one_deegre(
    id: int, service: Annotated[DeegreService, Depends(deegre_service)]
):
    """Эндпоинт для удаления уровня образования."""
    try:
        id = await service.delete(id)
        return SuccesDeleteSchema(id=id)
    except ItemNotFoundError:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content=ItemNotFoundSchema().model_dump(),
        )
    except UniversalError as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=UniversalErrorSchema(details=e.__str__()).model_dump(),
        )
