from fastapi import APIRouter

from backend.app.api.routes import entity
from backend.app.api.routes import item
from backend.app.api.routes import relation

api_router = APIRouter()

api_router.include_router(entity.router, prefix="/entity", tags=["entity"])
api_router.include_router(relation.router, prefix="/relation", tags=["relation"])
api_router.include_router(item.router, prefix="/item", tags=["item"])
