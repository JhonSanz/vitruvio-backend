from fastapi import APIRouter

from backend.app.api.routes import entity
from backend.app.api.routes import item

api_router = APIRouter()

api_router.include_router(entity.router, prefix="/entity", tags=["entity"])
api_router.include_router(item.router, prefix="/item", tags=["item"])
