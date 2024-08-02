from typing import List, Optional
from fastapi import APIRouter, HTTPException
from backend.app.api.crud import graph as create_graph
from backend.app.api.schemas.graph import DataModel, DataInsumos



router = APIRouter()


@router.post("/")
def receive_data(data_model: DataModel):
    try:
        create_graph.create_graph(data_model)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create graph {e}")


@router.post("/insumo")
def create_insumo(data_model: DataInsumos):
    try:
        create_graph.create_insumo(data_model)
        return 200
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create graph {e}")
