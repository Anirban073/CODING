from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None


class ProductOut(BaseModel):
    name: str
    price: float



# # without return type
# @app.get("/products/")
# async def get_products():
#     return[
#         {"status" : "ok"},
#         {"status" : 200}
#     ] 



# # return type annotation
# @app.get("/products/")
# async def get_products() -> Product:
#     return{
#         'id' : 1,
#         "name" : "moto-e",
#         "price" : 82892,
#         "stock" : 73
#     }



# @app.get("/products/")
# async def get_products() -> list[Product]:
#     return[
#         {'id' : 1,"name" : "moto-e","price" : 82892,"stock" : 73},
#         {'id' : 41,"name" : "vivo","price" : 92,"stock" : 7, "description": "anirban chakraborty"}
#     ]



# @app.post("/products/")
# async def create_product(product: Product) -> ProductOut:
#     return product


class BaseUser(BaseModel):
    username : str
    full_name : str | None = None


class UserIn(BaseUser):   #inheritance
    password : str


@app.post("/users/")
async def create_user(user: UserIn) -> BaseUser:
    return user