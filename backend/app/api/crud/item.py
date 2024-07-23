from typing import List
from backend.app.database.models import Item
from backend.app.api.schemas.item import ItemCreate, ItemUpdate
from neomodel import db


def get_item(*, item_id: int) -> Item:
    pass

def get_items(*, skip: int = 0, limit: int = 10) -> List[Item]:
    pass

def create_item(*, item: ItemCreate):
    label = item.label
    properties = item.properties

    query = f"CREATE (n:{label} $properties) RETURN n"
    params = {"properties": properties}

    try:
        db.cypher_query(query, params=params)
        return {"message": "Node created successfully", "data": f"(n:{label} {properties})"}
    except Exception as e:
        raise e


def update_item(*, item_id: int, item: ItemUpdate) -> Item:
    pass


def delete_item(*, item_id: int) -> bool:
    pass