from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

app = FastAPI()

fruits = {
    "apple" : "a juicy fruit",
    'banana' : "a yellow delight"
}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc:RequestValidationError):
    return PlainTextResponse(str(exc), status_code = 400)

@app.get("items/{item_id}")
async def read_items(item_id : int):
    return item_id