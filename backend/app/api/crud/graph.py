from backend.app.api.crud.item import create_item
from backend.app.api.crud.relation import create_relation_graph
from backend.app.api.schemas.graph import DataModel, DataInsumos
from backend.app.api.schemas.item import ItemCreate
from backend.app.api.schemas.relation import RelationCreateInsumo


def create_graph(data_model: DataModel):
    for item in data_model.data:
        label = item.name        
        for i, node in enumerate(item.data):
            if node:
                create_item(item=ItemCreate(label=label, code=f"{label}{node["name"]}{i}", properties=node))


def create_insumo(data_model: DataInsumos):
    processed_params = {item.name:item.value for item in data_model.nodeParams}
    node = ItemCreate(label=data_model.name, code=data_model.code, properties=processed_params)
    create_item(item=node)
    for rel in data_model.nodeRelations:
        create_relation_graph(relation=RelationCreateInsumo(
            relation_name="HAS",
            origin_code=node.code,
            target_code=rel.related,
            properties=rel.params
        ))
