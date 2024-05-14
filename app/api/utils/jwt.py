from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError

SECRET_KEY="77f087b2a4a35cf86ef3b33e975787fc1174c1717da6df7c4153c119b31c0726"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRY_MINUTES = 400

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None