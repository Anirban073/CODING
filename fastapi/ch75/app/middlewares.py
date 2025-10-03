from fastapi import Request

# first middleware
async def users_only_middleware(request: Request, call_next):
    if request.url.path.startswith("/users"):
        print("user Middleware : before processing the request")
        response = await call_next(request)
        print("user Middleware : After processing the request, before returning response")
        return response
    else:
        print(f"user Middlewire : skipping middleware for {request.url.path}")
        response = await call_next(request)
        return response


# second middleware
async def products_only_middleware(request: Request, call_next):
    if request.url.path.startswith("/products"):
        print("product Middleware : before processing the request")
        response = await call_next(request)
        print("product Middleware : After processing the request, before returning response")
        return response
    else:
        print(f"product Middlewire : skipping middleware for {request.url.path}")
        response = await call_next(request)
        return response
    

async def my_middleware(request: Request, call_next):
        print("my Middleware : before processing the request")
        response = await call_next(request)
        print("my Middleware : After processing the request, before returning response")
        return response
