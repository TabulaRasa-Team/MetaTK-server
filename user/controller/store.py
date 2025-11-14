from typing import List
from fastapi import APIRouter

from user.model.store import StoreDetailedResponse, StoreListItem, StoreInfoResponse
from user.service import store as service

router = APIRouter(prefix="/api/user/store")

@router.get("/", response_model=List[StoreListItem])
def get_all_stores():
    return service.get_all_stores()

@router.get("/detailed/{store_id}")
def get_store_detailed(store_id: str) -> StoreDetailedResponse:
    return service.get_store_detailed(store_id)

@router.get("/{store_id}")
def get_store_info(store_id: str) -> StoreInfoResponse:
    return service.get_store_info(store_id)