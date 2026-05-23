from jose import jwt
from fastapi import Depends, HTTPException
from app.core.config import oauth2_scheme
from app.core.security import SECRET_KEY, ALGORITHM
from app.database.db import SessionLocal
from sqlalchemy.orm import Session

def get_current_user(token: str = Depends(oauth2_scheme)):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
        
def admin_only(
    current_user = Depends(get_current_user)
):

    if current_user["role"] != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()