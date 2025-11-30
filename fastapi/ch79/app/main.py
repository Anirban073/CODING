from fastapi import FastAPI
from app.user.routers import router as user_router
from app.product.routers import router as product_routers

app = FastAPI()

app.include_router(user_router)
app.include_router(product_routers)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the API"}