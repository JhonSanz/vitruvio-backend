from typing import List
from app.database.models import Item
from app.api.schemas.item import ItemCreate, ItemUpdate
from neomodel import db


def get_item(*, item_id: int) -> Item:
    pass

def get_items(*, skip: int = 0, limit: int = 10) -> List[Item]:
    pass

def create_item(*, item: ItemCreate):
    label = item.label
    properties = item.properties

    query = f"CREATE (:{label} $properties)"
    params = {"properties": properties}

    try:
        result = db.cypher_query(query, params=params)
        print(result)
        return result
    except Exception as e:
        raise e


def update_item(*, item_id: int, item: ItemUpdate) -> Item:
    pass


def delete_item(*, item_id: int) -> bool:
    pass