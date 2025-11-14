from enum import Enum
from typing import List
from pydantic import BaseModel

class SortType(str, Enum):
    RECENT = "recent"
    OLD = "old"
    EXPIRATION = "expiration"

class UseCouponRequest(BaseModel):
    coupon_id: str

class UseCouponResponse(BaseModel):
    message: str

class CouponItem(BaseModel):
    coupon_id: str
    coupon_name: str
    store_name: str
    expiration: str
    store_type: str

class CouponListResponse(BaseModel):
    coupons: List[CouponItem]

class CouponDetailResponse(BaseModel):
    coupon_id: str
    coupon_name: str
    store_name: str
    expiration: str
    store_type: str