# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()

# # nested body models
# class Category(BaseModel):
#     name : str = Field(
#         a = "name",
#         des = "dgah",
#         max_length=50
#     )

#     desciption : str | None = Field(
#         default = None,
#         av = "name bolll",
#         des = "aaaa",
#         max_length=10
#     )


# # model which use sub model
# class Product(BaseModel):
#     name : str = Field(
#         a = "name",
#         des = "dgah",
#         max_length=50
#     )

#     desciption : str | None = Field(
#         default = None,
#         av = "name bolll",
#         des = "aaaa",
#         max_length=10
#     )

#     category : Category | None = Field(
#         default = None,
#         title = "product name",
#         description = "frw fhgtf w"
#     )


# @app.post("/products")
# async def create_product(product:Product):
#     return product





from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# nested body models
# sub model
class Category(BaseModel):
    name : str = Field(
        title = "product name",
        description = 'the name of the product category',
        max_length = 50,
        min_length=1
    )

    description : str | None = Field(
        default = None,
        title = 'category description',
        description = "a brief description of the category",
        max_length = 200
    )


# model which will use submodel
# class Product(BaseModel):
#     name : str = Field(
#         title = "product name",
#         description = 'the name of the product',
#         max_length = 100,
#         min_length=1
#     )

#     price : float = Field(
#         gt = 0,
#         title = 'product price',
#         description = 'the price of the product in usd, must be greater than 0',
#     )

#     stock : int | None = Field(
#         default = None,
#         ge = 0,
#         title = "stock quentity",
#         description = "the number of items in stock, must be non negetive"
#     )

#     category : Category | None = Field(
#         default = None,
#         title='product category',
#         description = 'the category to which the product belongs'
#     )


class Product(BaseModel):
    name : str = Field(
        title = "product name",
        description = 'the name of the product',
        max_length = 100,
        min_length=1
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

    category : list[Category] | None = Field(
        default = None,
        title='product category',
        description = 'the category to which the product belongs'
    )

@app.post("/product")
async def create_product(product:Product):
    return product