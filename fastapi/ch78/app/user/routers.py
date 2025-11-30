from fastapi import APIRouter

router = APIRouter()

@router.get("users")
async def get_all_users():
    return {"data" : "all users"}

@router.get("/users/me")
async def get_current_user():
    return {"data" : "current user"}

@router.get("/users/{user_id}")
async def get_single_user(user_id: int):
    return {"data": "single user"}