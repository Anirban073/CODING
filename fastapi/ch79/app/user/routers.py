from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["users"])
async def get_all_users():
    return {"data": "all users"}

@router.get("/me", tags=["users"])
async def get_current_user():
    return {"data": "current user"}

@router.get("/{user_id}", tags=["users"])
async def get_single_user(user_id: int):
    return {"data": f"single user {user_id}"}
