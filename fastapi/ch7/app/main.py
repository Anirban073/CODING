from fastapi import FastAPI

app = FastAPI()

## order matters

@app.get("/product/road_nt_usb")
async def single_product():
    return{
        "response" : "single data fetched"
    }



@app.get("/product/{product_title}")
async def single_product(product_title : str):
    return{
        "response" : "single data fetched", "product_title" : product_title
    }