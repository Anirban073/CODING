from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# nested body models
class Category(BaseModel):
    name : str = Field(
        a = "name",
        des = "dgah",
        max_length=50
    )

    desciption : str | None = Field(
        default = None,
        av = "name bolll",
        des = "aaaa",
        max_length=10
    )


# model which use sub model
class Product(BaseModel):
    name : str = Field(
        a = "name",
        des = "dgah",
        max_length=50
    )

    desciption : str | None = Field(
        default = None,
        av = "name bolll",
        des = "aaaa",
        max_length=10
    )

    category : Category | None = Field(
        default = None,
        title = "product name",
        description = "frw fhgtf w"
    )


@app.post("/products")
async def create_product(product:Product):
    return product