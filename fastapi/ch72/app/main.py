from fastapi import FastAPI, Request

app = FastAPI()

# creating middleware
@app.middleware("http")
async def my_first_middleware(request: Request, call_next):
    print("Middleware : before processing the request")
    print(f"Request: {request.method} {request.url}")

    response = await call_next(request)

    print("Middleware : After processing the request, before returning response")
    print(f"Response status code: {response.status_code}")

    return response


@app.get("/users")
async def get_users():
    print("Endpoint: inside get_users endpoint")
    return {"data": "all users data"}