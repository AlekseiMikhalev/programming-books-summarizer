from fastapi import Depends, FastAPI, status, HTTPException
from pydantic import BaseModel, HttpUrl
from sqlalchemy.orm import Session

import router
import models
import schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

summarizer_app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@summarizer_app.get('/', status_code=status.HTTP_200_OK)
async def root():
    return {
        "application": "Programming Books Summarizer",
        "description": "Application for summarization programming books",
        "author": "Aleksei Mikhalev"
    }


@summarizer_app.post('/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = router.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Email already registered')
    return router.create_user(db=db, user=user)


@summarizer_app.get('/users/', response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = router.get_users(db, skip=skip, limit=limit)
    return users


@summarizer_app.get('/users/{user_id}', response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = router.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@summarizer_app.post('/users/{user_id}/books/', response_model=schemas.Book)
def create_book_for_user(
    user_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)
):
    return router.create_book(db=db, book=book, user_id=user_id)


@summarizer_app.get('/books/', response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = router.get_books(db, skip=skip, limit=limit)
    return books
