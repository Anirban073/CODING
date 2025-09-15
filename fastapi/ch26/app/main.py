from fastapi import FastAPI
from pydantic import BaseModel
from typing import List,Any, Optional
app = FastAPI()

# excluding unset default values
products_db = {
    "1":{"id":"1", "name";"laptop", "price":29.3, "stock":20, "is_active":True},

    "2":{"id":"2", "name";"phone", "price":219.3, "stock":210, "is_active":False}
}

class Product(BaseModel):
    id:str
    name:str
    price:float
    description:Optional[str] = None
    tax: float = 15.0  #default tax rate


@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id:str):
    return products_db.get(product_id, {})