from fastapi import FastAPI
from app.user.routers import router as user_router
from app.product.routers import router as product_routers

app = FastAPI()

app.include_router(user_router)
app.include_router(product_routers)

# @app.get("users")
# async def get_all_users():
#     return {"data" : "all users"}

# @app.get("/users/me")
# async def get_current_user():
#     return {"data" : "current user"}

# @app.get("/users/{user_id}")
# async def get_single_user(user_id: int):
#     return {"data": "single user"}

# @app.get("/products")
# async def get_all_products():
#     return {"data" : "all products"}

# @app.get("/products/{product_id}")
# async def get_single_product(product_id: int):
#     return {"data" : "single product"}