from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from app.db.models import User
from sqlalchemy.orm import Session
from app.api.utils.password import verify_password, get_password_hash
from app.api.utils.jwt import create_access_token
from app.db.base import get_session
from app.api.utils.response import success_response, error_response
from datetime import datetime, timedelta

router = APIRouter()


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


@router.post("/register")
async def register(user: UserCreate, db: Session = Depends(get_session)):
    if db.query(User).filter(User.email == user.email).first():
        return error_response("Email already in Use", status.HTTP_400_BAD_REQUEST)
    new_user = User(username=user.username, email=user.email)
    new_user.set_password(user.password)
    db.add(new_user)
    db.commit()

    access_token_expires = timedelta(minutes=400)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return success_response("Registration Successful", {"access_token": access_token})


@router.post("/login")
async def login(username: str, password: str, db: Session = Depends(get_session)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not user.check_password(password):
        return error_response("Invalid username or password", status.HTTP_401_UNAUTHORIZED)
    access_token_expires = timedelta(minutes=400)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return success_response("Login Successful", {"access_token": access_token})
