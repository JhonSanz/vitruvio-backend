from typing import List
from backend.app.database.models import Item
from backend.app.api.schemas.item import ItemCreate, ItemUpdate
from neomodel import db


def get_item(*, item_id: int) -> Item:
    pass

def get_items(*, entity: str, code: str | None) -> List[Item]:
    query = "MATCH (n)"
    conditions = []

    if entity:
        conditions.append(f"n:{entity}")
    if code:
        conditions.append(f"n.code = '{code}'")
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    query += " RETURN n"

    try:
        result, _ = db.cypher_query(query)
        nodes = [record[0] for record in result]
        return nodes
    except Exception as e:
        print(f"Failed to fetch nodes: {str(e)}")
        return []

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