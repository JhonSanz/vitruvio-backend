from typing import List
from app.database.models import Entity
from app.api.schemas.entity import EntityCreate, EntityUpdate


def get_entity(*, entity_id: int) -> Entity:
    pass

def get_entities(*, skip: int = 0, limit: int = 10) -> List[Entity]:
    pass

def create_entity(*, entity: EntityCreate) -> Entity:
    pass

def update_entity(*, entity_id: int, entity: EntityUpdate) -> Entity:
    pass

def delete_entity(*, entity_id: int) -> bool:
    pass