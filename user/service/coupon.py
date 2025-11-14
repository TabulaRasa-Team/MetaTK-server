from fastapi import HTTPException
from user.repository import coupon as repository
from user.model.coupon import UseCouponResponse, CouponListResponse, CouponDetailResponse, CouponItem, SortType

FIXED_USER_ID = "96e8096e-c169-11f0-9219-ca5403729248"

def use_coupon(coupon_id: str) -> UseCouponResponse:
    # 1. coupon_history에서 쿠폰 조회
    coupon_history = repository.get_coupon_history(FIXED_USER_ID, coupon_id)

    # 2. 쿠폰이 없으면 404
    if not coupon_history:
        raise HTTPException(status_code=404, detail="해당 쿠폰을 찾을 수 없습니다.")

    # 3. 이미 사용된 쿠폰이면 409
    if coupon_history['status'] == 'used':
        raise HTTPException(status_code=409, detail="이미 사용된 쿠폰입니다.")

    # 4. 쿠폰 상태를 'used'로 변경
    repository.update_coupon_status(FIXED_USER_ID, coupon_id, 'used')

    return UseCouponResponse(message="success")

def get_my_coupons(sort: str) -> CouponListResponse:
    # sort 파라미터 유효성 검사
    try:
        SortType(sort)
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail="sort 파라미터 값이 유효하지 않습니다. (허용 값: recent, old, expiration)"
        )

    coupons_data = repository.get_my_coupons(FIXED_USER_ID, sort)

    coupons = []
    for coupon_data in coupons_data:
        coupons.append(CouponItem(
            coupon_id=coupon_data['coupon_id'],
            coupon_name=coupon_data['coupon_name'],
            store_name=coupon_data['store_name'],
            expiration=str(coupon_data['expiration']),
            store_type=coupon_data['store_type']
        ))

    return CouponListResponse(coupons=coupons)

def get_coupon_detail(coupon_id: str) -> CouponDetailResponse:
    coupon_data = repository.get_coupon_detail(FIXED_USER_ID, coupon_id)

    if not coupon_data:
        raise HTTPException(status_code=404, detail="해당 쿠폰을 찾을 수 없습니다.")

    return CouponDetailResponse(
        coupon_id=coupon_data['coupon_id'],
        coupon_name=coupon_data['coupon_name'],
        store_name=coupon_data['store_name'],
        expiration=str(coupon_data['expiration']),
        store_type=coupon_data['store_type']
    )

def get_store_coupons(store_id: str, sort: str) -> CouponListResponse:
    # sort 파라미터 유효성 검사
    try:
        SortType(sort)
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail="sort 파라미터 값이 유효하지 않습니다. (허용 값: recent, old, expiration)"
        )

    coupons_data = repository.get_store_coupons(FIXED_USER_ID, store_id, sort)

    coupons = []
    for coupon_data in coupons_data:
        coupons.append(CouponItem(
            coupon_id=coupon_data['coupon_id'],
            coupon_name=coupon_data['coupon_name'],
            store_name=coupon_data['store_name'],
            expiration=str(coupon_data['expiration']),
            store_type=coupon_data['store_type']
        ))

    return CouponListResponse(coupons=coupons)