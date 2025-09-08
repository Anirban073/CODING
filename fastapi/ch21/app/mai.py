from fastapi import FastAPI, Cookie, Body
from typing import Annotated
from pydantic import Basemodel, Field
app = FastAPI()

class ProductCookies(Basemodel):
    session_id : str
    preferred_category : str | None = None
    tracking_id : str | None = None

@app.get("/products/recommendations")
async def get_recommendations(cookies : Annotated[ProductCookies, Cookie()]):
    if cookies.preferred_category : 