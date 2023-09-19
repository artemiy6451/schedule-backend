"""Файл с эндпоинтами для для структурного подразделения."""
from typing import Annotated

from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from app.exceptions import ItemAlreadyExistError, ItemNotFoundError, UniversalError
from app.schemas import (
    ItemAlreadyExistSchema,
    ItemNotFoundSchema,
    SuccesAddSchema,
    SuccesDeleteSchema,
    UniversalErrorSchema,
)
from app.structure.dependencies import structure_service
from app.structure.schemas import StructureSchemaAdd, StructureSchemaGet
from app.structure.services import StructureService

router = APIRouter(prefix="/structure", tags=["Structure"])


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": SuccesAddSchema},
        status.HTTP_409_CONFLICT: {"model": ItemAlreadyExistSchema},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": UniversalErrorSchema},
    },
)
async def add_structure(
    structure: StructureSchemaAdd,
    service: Annotated[StructureService, Depends(structure_service)],
):
    """Эндпоинт для добавления структурного подразделения в базу данных."""
    try:
        id = await service.add(structure)
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


@router.get("", responses={status.HTTP_200_OK: {"model": StructureSchemaGet}})
async def get_all_structure(
    service: Annotated[StructureService, Depends(structure_service)]
):
    """Эндпоинт для получения всех стурктурных подразделений."""
    res = await service.get_all()
    return StructureSchemaGet(data=res)


@router.put(
    "/{id}",
    responses={
        status.HTTP_200_OK: {"model": StructureSchemaGet},
        status.HTTP_409_CONFLICT: {"model": ItemNotFoundSchema},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": UniversalErrorSchema},
    },
)
async def update_one_structure(
    id: int,
    structure: StructureSchemaAdd,
    service: Annotated[StructureService, Depends(structure_service)],
):
    """Эндпоинт для обновления стурктурного подразделения."""
    try:
        res = await service.update(id, structure)
        return StructureSchemaGet(data=res)
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
async def delete_one_structure(
    id: int, service: Annotated[StructureService, Depends(structure_service)]
):
    """Эндпоинт для удаления структурного подразделения."""
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
