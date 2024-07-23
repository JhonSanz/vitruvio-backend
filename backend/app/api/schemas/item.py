from pydantic import BaseModel
from typing import Any, Dict


class ItemBase(BaseModel):
    label: str
    code: str
    properties: Dict[str, Any]


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class Item(ItemBase):
    class Config:
        orm_mode = True
