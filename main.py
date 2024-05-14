from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.api.auth import router as auth_router

# create fast api instance
app = FastAPI()


app.include_router(auth_router, prefix="/api/v1/auth")

