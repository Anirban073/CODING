from fastapi import FastAPI

app = FastAPI()

# parameter with type

# @app.get("/product/{product_id}")

# async def single_product(product_id):
#     return{
#         "response" : "single data fetched", "product_id" : product_id
#     }


@app.get("/product/{product_id}")

async def single_product(product_id : int):
    return{
        "response" : "single data fetched", "product_id" : product_id
    }