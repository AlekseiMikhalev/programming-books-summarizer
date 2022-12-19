
from fastapi import Depends, HTTPException
from fastapi import APIRouter

from users.schemas import UserBase, UserCreate, UserInfo
from sqlalchemy.orm import Session

from database.session import get_db
from users.service import get_user_by_email, create_user, get_users

from auth.service import get_current_user


router = APIRouter(tags=['users'])


@router.post('/users/create', response_model=UserInfo)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.get('/users/get', response_model=list[UserInfo])
def read_users(limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db=db, limit=limit)
    return users


@router.get('/users/me', response_model=UserInfo)
async def read_users_me(current_user: UserBase = Depends(get_current_user)):
    return current_user
