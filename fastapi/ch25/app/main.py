from fastapi import FastAPI
from pydantic import BaseModel
from typing import List,Any
app = FastAPI()

class Product(BaseModel):
    id : int
    name : str
    price : float
    stock : int | None = None

class ProductOut(BaseModel):
    name : str
    price : float

# # without response_model parameter
# @app.get("/products/")
# async def get_products():
#     return{
#         "id":1, 'name':"moto-e", "price":28.22, "stock":5
#     }


# # with response_model parameter
# @app.get("/products/", response_model = Product)
# async def get_products():
#     return{
#         "id":1, 'name':"moto-e", "price":28.22, "stock":5
#     }



# @app.get("/products/", response_model = list[Product])
# async def get_products():
#     return[
#         {
#         "id":1, 'name':"moto-e", "price":28.22, "stock":5
#         },
#         {
#         "id":12, 'name':"vivo-e", "price":28.22, "stock":15, "description" : "anirban"
#         }
#     ]



class BaseUser(BaseModel):
    username : str
    full_name : str | None = None


class UserIn(BaseUser):   #inheritance
    password : str


# @app.post("/users/", response_model = BaseUser)
# async def create_user(user: UserIn):
#     return user


# @app.post('/products/', response_model=Product)  #more priority than any
# async def create_product(product:Product) -> Any:
#     return product


@app.post('/products/', response_model=None)  #more priority than any
async def create_product(product:Product) -> Any:
    return product