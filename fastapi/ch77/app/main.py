from fastapi import FastAPI
from app.middlewares import CustomLoggingMiddleware

app = FastAPI()

# app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(CustomLoggingMiddleware, prefix="CUSTOM_LOG")

@app.get("/users")
async def get_users():
    print("Endpoint: inside get_users endpoint")
    return {"data": "all users data"}

@app.get("/products")
async def get_products():
    print("Endpoint: inside get_products endpoint")
    return {"data": "all products data"}