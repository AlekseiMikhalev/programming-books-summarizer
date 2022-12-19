from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserInfo(UserBase):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True
