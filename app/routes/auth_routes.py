from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.services.auth_service import (
    register_user,
    login_user
)

from app.schemas.auth_schema import RegisterSchema

from app.core.dependencies import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
def register(
    user: RegisterSchema,
    db: Session = Depends(get_db)
):

    return register_user(db, user)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        form_data.username,
        form_data.password
    )

    if not token:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }