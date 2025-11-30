from fastapi import FastAPI, Depends
from typing_extensions import Annotated

app = FastAPI()

# creating dependency function
async def common_parametrs(q: str | None=None, skip: int=0, limit: int=100):
    return {"q" : q, "skip": skip, "limit": limit}

# using dependency in endpoints
@app.get("/items")
async def read_items(commons: Annotated[dict, Depends(common_parametrs)]):
    return commons


@app.get("/users")
async def read_users(commons: Annotated[dict, Depends(common_parametrs)]):
    return commons

# create a type alias
commonsDep = Annotated[dict, Depends(common_parametrs)]

@app.get("/products")
async def read_products(commons: commonsDep):
    return commons

@app.get("/carts")
async def read_carts(commons: commonsDep):
    return commons