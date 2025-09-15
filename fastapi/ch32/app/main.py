from fastapi import FastAPI, HTTPException
app = FastAPI()

items = {
    "apple" : "a juicy fruit",
    'banana' : "a yellow delight"
}

# using HTTPException
# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="item not found")
#     return items[item_id]


# adding custom header
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="item not found",
        headers = {"x-error-type" : "itemMissing"}
        )
    return items[item_id]