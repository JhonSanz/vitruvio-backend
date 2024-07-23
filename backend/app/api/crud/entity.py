from typing import List
from backend.app.api.schemas.entity import EntityCreate, EntityUpdate
from neomodel import db


def get_entity(*, entity_id: int):
    pass

def get_entities(*, skip: int = 0, limit: int = 10):
    query = "CALL db.labels()"
    try:
        result = db.cypher_query(query)
        labels = [record[0] for record in result]
        return labels
    except Exception as e:
        print(f"Failed to fetch node labels: {str(e)}")
        return []

def create_entity(*, entity: EntityCreate):
    pass

def update_entity(*, entity_id: int, entity: EntityUpdate):
    pass

def delete_entity(*, entity_id: int):
    pass