from pydantic import BaseModel
from typing import Any, Dict, List


class ItemBase(BaseModel):
    labels: List[str]
    properties: Dict[str, Any]


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class Item(ItemBase):
    class Config:
        orm_mode = True
