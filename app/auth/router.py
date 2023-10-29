"""Файл с эндпоинтами модуля `auth`."""

from fastapi_users import FastAPIUsers

from app.auth.models import User
from app.auth.services import auth_backend, get_user_manager

router = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
).get_auth_router(auth_backend)
