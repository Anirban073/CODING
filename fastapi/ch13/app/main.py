from fastapi import FastAPI,Query
from typing import Annotated
from pydantic import AfterValidator
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

# # BASIC QUERY PARAMETER
# @app.get("/products")
# async def get_products(search : str | None = None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS


# # VALIDATION WITHOUT ANNOTATED
# @app.get("/products")
# async def get_products(search : str | None = Query(default=None, max_length=5)):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS


# # VALIDATION WITH ANNOTATED
# @app.get("/products")
# async def get_products(
#     search :
#         Annotated[
#             str | None,
#             Query(max_length=5, min_length=3, pattern = "^[a-z]+$")
#             ] = None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS


# # MULTIPLE SEARCH TERMS(LIST)
# @app.get("/products")
# async def get_products(search: Annotated[list[str] | None, Query()] = None):
#     if search:
#         filtered_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS



# ALIAS PARAMETERS
# @app.get("/products")
# async def get_products(search: Annotated[str | None, Query(alias = "p")] = None):
#     if search:
#         filtered_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS



# # ADDING METADATA
# @app.get("/products")
# async def get_products(search: Annotated[
#     str | None,
#     Query(alias = "p", title = "search_products", description="search by product title")
#     ] = None):
#     if search:
#         filtered_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS


# # deprecating parameters
# @app.get("/products")
# async def get_products(search: Annotated[
#     str | None,
#     Query(deprecated = True)
#     ] = None):
#     if search:
#         filtered_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS


# CUSTOM VALIDATION
def check_valid_id(id: str):
    if not id.startswith("prod-"):
        raise ValueError("ID must be with 'prod-'")
    return id


@app.get("/products")
async def get_products(id: Annotated[
    str | None,
    AfterValidator(check_valid_id)] = None):
    if id:
        return{"id" : id, "message" : "valid product id"}
    return{"message": "No ID provided"}