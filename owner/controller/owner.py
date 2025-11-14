from fastapi import APIRouter, Body, HTTPException

from core.error import DuplicateResourceException, InvalidValueException, IdNotFoundException
from owner.model.owner import Store, Coupon, MenuRequest
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

@router.post("/coupon")
def create_coupon(request: Coupon = Body()) -> dict:
    try:
        return service.create_coupon(request)
    except IdNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.msg)