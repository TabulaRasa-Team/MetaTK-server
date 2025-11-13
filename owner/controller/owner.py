from fastapi import APIRouter, Body

from owner.model.owner import Store
from owner.service import owner as service

router = APIRouter(prefix="/api/owner")

@router.post("/store")
def create_store(request: Store = Body()) -> dict:
    return service.create_store(request)

@router.post("/store/menu")
def create_menu():
    return {"message": "POST /api/owner/store/menu"}

@router.post("/store/photo")
def create_store_photo():
    return {"message": "POST /api/owner/store/photo"}

@router.post("/coupon")
def create_coupon():
    return {"message": "POST /api/owner/coupon"}