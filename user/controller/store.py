from fastapi import APIRouter

from user.model.store import StoreDetailedResponse
from user.service import store as service

router = APIRouter(prefix="/api/user/store")

@router.get("/detailed/{store_id}")
def get_store_detailed(store_id: str) -> StoreDetailedResponse:
    return service.get_store_detailed(store_id)

@router.get("/{store_id}")
def get_store(store_id: str):
    return {"message": f"GET /api/user/store/{store_id}"}