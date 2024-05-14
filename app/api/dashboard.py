from fastapi import APIRouter, Depends
from app.api.utils.jwt import get_current_user
from app.api.utils.response import success_response

router = APIRouter()


@router.get("/")
async def dashboard(current_user: dict = Depends(get_current_user)):
    return success_response("Dashboard data retrieved successfully", data=current_user)
