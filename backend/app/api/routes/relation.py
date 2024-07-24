from typing import List, Optional
from fastapi import APIRouter, HTTPException
from backend.app.api.crud import relation as crud_relation
from backend.app.api.schemas.item import Item
from backend.app.api.schemas.relation import (
    RelationBase,
    RelationCreate,
    RelationUpdate,
    Relation,
    RelationGet
)

router = APIRouter()



@router.post("/", response_model=Relation)
def create_relation(relation: RelationCreate):
    print("aqui estoy")
    created_relation = crud_relation.create_relation(relation=relation)
    print("created_relation", created_relation)
    if created_relation:
        return True
    else:
        raise HTTPException(status_code=500, detail="Failed to create relation")


@router.get("/", response_model=List[Item])
def get_related_nodes(origin_code: str):
    print("aqui estoy")
    related_nodes = crud_relation.get_related_nodes(origin_code=origin_code)
    print("related_nodes", related_nodes)
    return related_nodes
