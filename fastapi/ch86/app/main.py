# from fastapi import FastAPI
# from app.routers import router
from fastapi import FastAPI, Depends
from app.routers import router, verify_token


app = FastAPI()

# dependencies for a group of path operations
# app.include_router(router)
app.include_router(router, dependencies= [Depends(verify_token)])