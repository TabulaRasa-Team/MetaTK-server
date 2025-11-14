from fastapi import APIRouter

router = APIRouter(prefix="/api/user/occupations")

@router.get("/")
def get_occupations():
    return {"message": "GET /api/user/occupations"}