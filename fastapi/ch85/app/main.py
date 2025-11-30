from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

# creating cdependency class
class commonQuaryParams:
    def __init__(self, q: str | None=None, skip: int=0, limit:int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

# using dependency in endpoints
@app.get("/items")
async def read_items(commons: Annotated[commonQuaryParams, Depends(commonQuaryParams)]):
    return commons

# create a type alias
commonDep = Annotated[commonQuaryParams, Depends(commonQuaryParams)]

@app.get("/products")
async def read_products(commons: commonDep):
    return commons