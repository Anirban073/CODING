from fastapi import FastAPI

app = FastAPI()

# single query parameter
# @app.get("/product")
# async def product(category:str):
#     return {"status" : "ok", "category" : category}


# multiple query parameter
@app.get("/product")
async def product(category:str, limit:int):
    return {"status" : "ok", "category" : category, "limit":limit}


# default query parameter
@app.get("/product")
async def product(category:str, limit:int=10):
    return {"status" : "ok", "category" : category, "limit":limit}


# optional query parameter
@app.get("/product")
async def product(limit:int, category:str | None = None):
    return {"status" : "ok", "category" : category, "limit":limit}


# path and query parameter
@app.get("/product/{year}")
async def product(year:str, category:str):
    return {"status" : "ok",
            "year":year, "category" : category}