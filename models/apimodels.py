from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=32)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=120)
    role: str = Field(..., min_length=3, max_length=15)
    mobile: str = Field(..., min_length=10, max_length=10)

class UserUpdate(BaseModel):
    username: Optional[str] = Field(default=None, min_length=3, max_length=32)
    email: Optional[EmailStr] = Field(default=None)
    password: Optional[str] = Field(default=None, min_length=6, max_length=120)
    role: Optional[str] = Field(default=None, min_length=3, max_length=15)
    mobile: Optional[str] = Field(default=None, min_length=10, max_length=10)

class UserResp(BaseModel):
    username: Optional[str] = Field(default=None, min_length=3, max_length=32)
    email: Optional[EmailStr] = Field(default=None)
    role: Optional[str] = Field(default=None, min_length=3, max_length=15)
    mobile: Optional[str] = Field(default=None, min_length=10, max_length=10)

class Token(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    username: str
    password: str