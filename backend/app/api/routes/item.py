from typing import List
from fastapi import APIRouter, HTTPException
from app.api.crud import item as crud_item
from app.api.schemas.item import (
    ItemBase,
    ItemCreate,
    ItemUpdate,
    Item,
)

router = APIRouter()


@router.get("/{item_id}", response_model=ItemBase)
def get_item(item_id: int):
    db_item = crud_item.get_item(item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.get("/item/", response_model=List[Item])
def get_items(skip: int = 0, limit: int = 10):
    items = crud_item.get_items(skip=skip, limit=limit)
    return items


@router.post("/", response_model=ItemBase)
def create_item(item: ItemCreate):
    return crud_item.create_item(item=item)


@router.put("/item/{item_id}", response_model=ItemBase)
def update_item(
    item_id: int, item: ItemUpdate
):
    db_item = crud_item.update_item(
        item_id=item_id, item=item
    )
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.delete("/item/{item_id}", response_model=bool)
def delete_item(item_id: int):
    success = crud_item.delete_item(item_id=item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return success
