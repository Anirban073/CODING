from fastapi import FastAPI, Request

app = FastAPI()

# creating middleware
# first middleware
@app.middleware("http")
async def my_first_middleware(request: Request, call_next):
    print("1st Middleware : before processing the request")
    response = await call_next(request)
    print("1st Middleware : After processing the request, before returning response")
    return response


# second middleware
@app.middleware("http")
async def my_second_middleware(request: Request, call_next):
    print("2nd Middleware : before processing the request")
    response = await call_next(request)
    print("2nd Middleware : After processing the request, before returning response")
    return response



@app.get("/users")
async def get_users():
    print("Endpoint: inside get_users endpoint")
    return {"data": "all users data"}