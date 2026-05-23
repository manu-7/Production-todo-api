from sqlalchemy.orm import Session

from app.models.user_model import User

from app.core.security import (
    verify_password,
    hash_password,
    create_access_token
)

def register_user(
    db: Session,
    user_data
):

    hashed_password = hash_password(
        user_data.password
    )

    user = User(
        username=user_data.username,
        email=user_data.email,
        password=hashed_password
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def login_user(
    db: Session,
    email: str,
    password: str
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return None

    if not verify_password(
        password,
        user.password
    ):
        return None

    token = create_access_token(
        {
            "user_id": user.id,
            "role": user.role
        }
    )

    return token