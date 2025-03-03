from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    email: EmailStr
    token: str

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    email: str | None = None  # Adjust fields as needed
