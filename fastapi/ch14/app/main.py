from fastapi import FastAPI,Path,Query
from typing import Annotated

app = FastAPI()

PRODUCTS = [
    {
        "id" : 1,
        "title" : "msi laptop",
        "price" : 108,
        "description" : "anirban's laptop" 
    },

    {
        "id" : 2,
        "title" : "asus laptop",
        "price" : 8000,
        "description" : "sourabh's laptop" 
    },

    {
        "id" : 3,
        "title" : "hp laptop",
        "price" : 7000,
        "description" : "bhola's laptop" 
    },
]

# # BASIC PATH PARAMETER
# @app.get("/products/{product_id}")
# async def get_product(product_id: int):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#         return{"error" : "product not found"}



# # NUMERIC VALIDATION
# @app.get("/products/{product_id}")
# async def get_product(product_id: Annotated[int, Path(ge = 1, le = 3)]):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return{"error" : "product not found"}



# # ADDING METADATA WITH PATH
# @app.get("/products/{product_id}")
# async def get_product(product_id: Annotated[int, Path(title="The ID of the product", description="This is product ID")]):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return{"error" : "product not found"}



# COMBINING PATH AND QUERY PARAMETERS
@app.get("/products/{product_id}")
async def get_product(
    product_id : Annotated[int, Path(gt=0, le=100)],
    search:Annotated[str | None, Query(max_lenget=20)] = None
):
    for product in PRODUCTS:
        if product["id"] == product_id:
            if search and search.lower() not in product["title"].lower():
                return{"Error" : "product does not match search term"}
            return product
    return{"error" : "product not found"}