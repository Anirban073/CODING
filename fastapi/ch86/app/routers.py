from fastapi import APIRouter, Header, HTTPException, Depends
from typing import Annotated


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "my-secret-token":
        raise HTTPException(status_code=400, detail="x token header invalid")

# router = APIRouter(dependencies= [Depends(verify_token)])
router = APIRouter()

@router.get("/items")
async def read_items():
    return{"data":"all items"}