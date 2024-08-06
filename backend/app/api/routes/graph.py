from typing import List, Optional
from fastapi import APIRouter, HTTPException
from backend.app.api.crud import graph as crud_graph
from backend.app.api.schemas.graph import DataModel, DataInsumos
from backend.app.api.crud.item import Item


router = APIRouter()


@router.post("/")
def receive_data(data_model: DataModel):
    try:
        crud_graph.create_graph(data_model)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create graph {e}")


@router.get("/", response_model=List[Item])
def get_items(direction: str | None = None):
    items = crud_graph.show_nodes(direction="")
    return items


@router.get("/node-children", response_model=List[Item])
def get_node_children(node_code: str):
    return crud_graph.get_node_children(code=node_code)


@router.post("/insumo")
def create_insumo(data_model: DataInsumos):
    print("route", data_model)
    try:
        crud_graph.create_insumo(data_model)
        return 200
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to create graph {e}")
