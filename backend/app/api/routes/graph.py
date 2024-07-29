from typing import List, Optional
from fastapi import APIRouter, HTTPException
from backend.app.api.crud import graph as create_graph
from backend.app.api.schemas.graph import DataModel



router = APIRouter()


@router.post("/")
def receive_data(data_model: DataModel):
    try:
        create_graph.create_graph(data_model)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create graph {e}")
