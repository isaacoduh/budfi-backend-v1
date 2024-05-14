from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.api.auth import router as auth_router
from app.api.dashboard import router as dashboard_router

# create fast api instance
app = FastAPI()


@app.get("/")
async def read_main():
    return {"message": "Hello World"}


app.include_router(auth_router, prefix="/api/v1/auth")
app.include_router(dashboard_router, prefix="/api/v1/dashboard")
