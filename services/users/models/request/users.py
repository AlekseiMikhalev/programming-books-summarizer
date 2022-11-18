from pydantic import BaseModel
from typing import Optional
from users.models.data.users import UserStatus


class SignupReq(BaseModel):
    user_id: int
    username: str
    password: str


class UserReq(BaseModel):
    user_id: int
    fname: str
    lname: str
    status: UserStatus


class UserDetails(BaseModel):
    fname: Optional[str] = None
    lname: Optional[str] = None
    status: Optional[UserStatus] = None
