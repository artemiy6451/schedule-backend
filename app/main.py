"""Стартовая точка приложения."""

from fastapi import APIRouter, FastAPI

from app.deegre.router import router as deegre_router

app = FastAPI(title="Schedule backend")

routers: list[APIRouter] = [
    deegre_router,
]

for router in routers:
    app.include_router(router)
