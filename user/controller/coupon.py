from fastapi import APIRouter

from user.model.coupon import UseCouponRequest, UseCouponResponse, CouponListResponse, CouponDetailResponse
from user.service import coupon as service

router = APIRouter(prefix="/api/user/my/coupon")

@router.get("/", response_model=CouponListResponse)
def get_my_coupons(sort: str):
    return service.get_my_coupons(sort)

@router.get("/store/{store_id}", response_model=CouponListResponse)
def get_store_coupons(store_id: str, sort: str):
    return service.get_store_coupons(store_id, sort)

@router.get("/{coupon_id}", response_model=CouponDetailResponse)
def get_coupon_detail(coupon_id: str):
    return service.get_coupon_detail(coupon_id)

@router.patch("/")
def update_my_coupon(request: UseCouponRequest) -> UseCouponResponse:
    return service.use_coupon(request.coupon_id)