from fastapi import APIRouter

router = APIRouter(prefix="/api/user/store")

@router.get("/detailed")
def get_store_detailed():
    return {"message": "GET /api/user/store/detailed"}

@router.get("/{store_id}")
def get_store(store_id: str):
    return {"message": f"GET /api/user/store/{store_id}"}