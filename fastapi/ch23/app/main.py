from fastapi import FastAPI, Header, Body
from typing import Annotated
from pydantic import BaseModel, Field
app = FastAPI()

# # headers with a pydantic model
# class ProductHeaders(BaseModel):
#     authorization : str
#     accept_language: str | None = None
#     x_tracking_id: list[str] = []

# @app.get("/products")
# async def get_product(headers: Annotated[ProductHeaders, Header()]):
#     return{
#         'headers' : headers
#     }



# forbidding extra headers
class ProductHeaders(BaseModel):
    model_config = {"extra" : "forbid"}
    authorization : str
    accept_language: str | None = None
    x_tracking_id: list[str] = []

@app.get("/products")
async def get_product(headers: Annotated[ProductHeaders, Header()]):
    return{
        'headers' : headers
    }