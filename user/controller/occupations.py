from fastapi import APIRouter

from user.service import occupations as service

router = APIRouter(prefix="/api/user/occupations")

@router.get("/")
def get_occupations() -> dict:
    return service.get_occupations()