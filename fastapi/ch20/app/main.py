from fastapi import FastAPI, Cookie
from typing import Annotated
app = FastAPI()

@app.get("/products")
async def get_recomendations(session_id:Annotated[str | None,Cookie()] = None):
    if session_id:
        return {"message" : "recomendation for session{session_id}", "session_id" : session_id}
    return {
        "message" : "no session id provided, showing default recomandations"
    }