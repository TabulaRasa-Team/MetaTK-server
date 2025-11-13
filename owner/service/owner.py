import uuid

from owner.model.owner import Store
from owner.repository import owner as repository

def create_store(request: Store) -> dict[str, str]:
    store_id = str(uuid.uuid4())
    store_type_value = request.category.value
    repository.create_store(store_id, store_type_value, request)

    return {
        "store_id" : store_id
    }
