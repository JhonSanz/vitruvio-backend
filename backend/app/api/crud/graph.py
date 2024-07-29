from backend.app.api.crud.item import create_item
from backend.app.api.schemas.graph import DataModel
from backend.app.api.schemas.item import ItemCreate


def create_graph(data_model: DataModel):
    for item in data_model.data:
        label = item.name        
        for i, node in enumerate(item.data):
            if node:
                create_item(item=ItemCreate(label=label, code=f"{label}{node["name"]}{i}", properties=node))
    