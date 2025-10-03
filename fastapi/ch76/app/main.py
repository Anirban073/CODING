from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

# app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["localhost", "127.0.0.1"])

@app.get("/users")
async def get_users():
    print("Endpoint: inside get_users endpoint")
    return {"data": "all users data"}

@app.get("/products")
async def get_products():
    print("Endpoint: inside get_products endpoint")
    return {"data": "all products data"}