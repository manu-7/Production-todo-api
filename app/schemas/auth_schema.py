from pydantic import BaseModel, EmailStr, Field
from passlib.context import CryptContext

class RegisterSchema(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(
        min_length=6,
        max_length=128
    )

class LoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=6,
        max_length=128
    )

class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    
pwd_context = CryptContext(
    schemes=["bcrypt_sha256"],
    deprecated="auto"
)