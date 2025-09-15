from fastapi import FastAPI,Header
from typing import Annotated
app = FastAPI()

# # header parameter
# @app.get("/products")
# async def get_products(user_agent : Annotated[str | None, Header()] = None):
#     return user_agent



# # handling duplicate headers
# @app.get("/products")
# async def get_product(x_product_token: Annotated[list[str] | None, Header()] = None):
#     return{
#          "x_product_token" : x_product_token or []
#     }