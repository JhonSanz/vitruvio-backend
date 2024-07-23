from typing import List
from fastapi import APIRouter, HTTPException
from app.api.crud import entity as crud_entity
from app.api.schemas.entity import (
    EntityBase,
    EntityCreate,
    EntityUpdate,
    Entity,
)

router = APIRouter()


@router.get("/{entity_id}", response_model=EntityBase)
def get_entity(entity_id: int):
    db_entity = crud_entity.get_entity(entity_id=entity_id)
    if db_entity is None:
        raise HTTPException(status_code=404, detail="Entity not found")
    return db_entity


@router.get("/entity/", response_model=List[Entity])
def get_entities(skip: int = 0, limit: int = 10):
    entities = crud_entity.get_entities(skip=skip, limit=limit)
    return entities


@router.post("/", response_model=EntityBase)
def create_entity(entity: EntityCreate):
    return crud_entity.create_entity(entity=entity)


@router.put("/entity/{entity_id}", response_model=EntityBase)
def update_entity(
    entity_id: int, entity: EntityUpdate
):
    db_entity = crud_entity.update_entity(
        entity_id=entity_id, entity=entity
    )
    if db_entity is None:
        raise HTTPException(status_code=404, detail="Entity not found")
    return db_entity


@router.delete("/entity/{entity_id}", response_model=bool)
def delete_entity(entity_id: int):
    success = crud_entity.delete_entity(entity_id=entity_id)
    if not success:
        raise HTTPException(status_code=404, detail="Entity not found")
    return success
