from fastapi import APIRouter, Body, HTTPException

from core.error import DuplicateResourceException, InvalidValueException
from owner.model.owner import Store
from owner.service import owner as service

router = APIRouter(prefix="/api/owner")

@router.post("/store")
def create_store(request: Store = Body()) -> dict:
    try:
        return service.create_store(request)
    except DuplicateResourceException as e:
        raise HTTPException(status_code=409, detail=e.msg)
    except InvalidValueException as e:
        raise HTTPException(status_code=400, detail=e.msg)

@router.post("/store/menu")
def create_menu():
    return {"message": "POST /api/owner/store/menu"}

@router.post("/store/photo")
def create_store_photo():
    return {"message": "POST /api/owner/store/photo"}

@router.post("/coupon")
def create_coupon():
    return {"message": "POST /api/owner/coupon"}