from fastapi import APIRouter

router = APIRouter(prefix="/api/user/my/coupon")

@router.get("/")
def get_my_coupon(sort: str): # 나중에 ENUM 형식으로 수정
    return {"message": "GET /api/user/my/coupon?sort={sort}"}

@router.get("/{coupon_id}")
def get_my_coupon(coupon_id: str):
    return {"message": f"GET /api/user/my/coupon/{coupon_id}"}

@router.patch("/")
def update_my_coupon():
    return {"message": f"PATCH /api/user/my/coupon"}