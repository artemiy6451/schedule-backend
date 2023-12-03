"""Файл с эндпонтами для модуля `direction`."""

from typing import Annotated

from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from app.direction.dependencies import direction_service
from app.direction.schemas import DirectionSchemaAdd
from app.direction.services import DirectionService
from app.exceptions import ItemAlreadyExistError, UniversalError
from app.schemas import ItemAlreadyExistSchema, SuccesAddSchema, UniversalErrorSchema

router = APIRouter(prefix="/direction", tags=["Direction"])


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": SuccesAddSchema},
        status.HTTP_409_CONFLICT: {"model": ItemAlreadyExistSchema},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": UniversalErrorSchema},
    },
)
async def add_direction(
    direction: DirectionSchemaAdd,
    service: Annotated[DirectionService, Depends(direction_service)],
):
    """Эндпоинт для добавления направления подготовки."""
    try:
        id = await service.add(direction)
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
