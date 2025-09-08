# from fastapi import FastAPI,Body
# from pydantic import BaseModel, Field
# from typing import Annotated

# app = FastAPI()

# # pydantic's Field
# class Product(BaseModel):
#     name : str = Field(
#         title = "product name",
#         description = "Anirban chakraborty",
#         max_length = 100,
#         min_length = 3,
#         pattern = "^[A-Za-z0-9]+$"
#     )

#     price : float = Field(
#         gt = 0,
#         title = "product price",
#         description = "nnnnnnnnnjhff"
#     )

#     stock : int | None = Field(
#         default= None,
#         ge = 0,
#         title = "stock quentity",
#         description = "aaaa"
#     )

# @app.post("/product")
# async def create_product(product : Product):
#     return product



from fastapi import FastAPI,Body
from pydantic import BaseModel, Field
from typing import Annotated
app = FastAPI()

# pydantic's field
class Product(BaseModel):
    name : str = Field(
        title = "product name",
        description = 'the name of the product',
        max_length = 100,
        min_length=3
        # pattern = "^[A-Za-z0-9]+$"
    )

    price : float = Field(
        gt = 0,
        title = 'product price',
        description = 'the price of the product in usd, must be greater than 0',
    )

    stock : int | None = Field(
        default = None,
        ge = 0,
        title = "stock quentity",
        description = "the number of items in stock, must be non negetive"
    )

@app.post("/product")
async def create_product(product:Product):
    return product

