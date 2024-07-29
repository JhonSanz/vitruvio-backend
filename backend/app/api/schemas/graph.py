from typing import List, Optional
from pydantic import BaseModel



class DataEntry(BaseModel):
    name: str
    data: List[dict]


class DataModel(BaseModel):
    data: List[DataEntry]

