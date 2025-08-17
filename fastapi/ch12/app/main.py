from fastapi import FastAPI,status

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

# GET Request
## read or fetch all data
@app.get("/product", status_code = status.HTTP_200_OK)
async def all_products():
    return PRODUCTS

# read of fetch single dta
@app.get("/product/{product_id}", status_code = status.HTTP_200_OK)
async def single_products(product_id : int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product

# post request
## create or insert data
@app.post("/product", status_code = status.HTTP_201_CREATED)
async def create_product(new_product : dict):
    PRODUCTS.append(new_product)
    return {"status" : "created", "new_product" : new_product}


# put request
## update complete data
@app.put("/product/{product_id}", status_code = status.HTTP_200_OK)
def update_product(product_id:int, new_update_product:dict):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS[index] = new_update_product
            return{"status":'updated',"product_id":product_id, "new updated product":new_update_product}
        
# delete request
## delete data
@app.delete("/product/{product_id}", status_code = status.HTTP_200_OK)
def delete_product(product_id:int):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS.pop(index)
            return{"status" : "data deleted", "product_id":product_id}