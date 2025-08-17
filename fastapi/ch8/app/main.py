from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# predefined values
# define an Enum class with allowed product categories
# class productCategory(str, Enum):
#     books = 'books'
#     clothing =  'clothing'
#     electronics = 'electronics'

# # use the Enum as the type for the path parameter
# @app.get("/products/{category}")
# async def get_products(category : productCategory):
#     return{
#         "response" : "products fetched", "category" : category
#     }



# working with python enumerations

class productCategory(str, Enum):
    books = 'books'
    clothing =  'clothing'
    electronics = 'electronics'


@app.get("/products/{category}")
async def get_products(category : productCategory):
    if category == productCategory.books:
        return{"category" : category, "message" : "books are awsome"}
    elif category.value == "clothing":
        return{"category" : category, "message" : "Fashion trends here!"}
    elif category == productCategory.electronics.value:
        return{"category" : category, "message" : "Latest gadget available here!"}
    else:
        return{"category" : category, "message" : "unknown category"}