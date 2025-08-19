from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# # using field-level examples
# class Product(BaseModel):
#     name : str = Field(examples = ["Moto E"])
#     price : float  = Field(examples = [23.90])
#     stock : int | None  = Field(default = None, examples =[43] )

# @app.post("/products")
# async def create_product(product : Product):
#     return product



# using pydantic's json_schema_extra
class Product(BaseModel):
    name : str
    price : float
    stock : int | None = None

    model_config = {
        "json_schema_extra" : {
            "examples" : [
                {
                "name" : "moto e",
                "price" : 27.24,
                "stock" : 45
                }
            ]
        }
    }

@app.post("/products")
async def create_product(product : Product):
    return product
