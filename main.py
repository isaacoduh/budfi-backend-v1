from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# create fast api instance
app = FastAPI()


# user Model for request body validation
class User(BaseModel):
    username: str
    password: str


# sample hardcoded users
fake_users_db = {
    "user1": {
        "username": "user1",
        "password": "password1"
    },
    "user2": {
        "username": "user2",
        "password": "password2"
    }
}


# login endpoint
@app.post("/api/auth/login")
def login(user: User):
    if user.username in fake_users_db:
        stored_user = fake_users_db[user.username]
        if user.password == stored_user['password']:
            return {"message": "Login Successful"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

