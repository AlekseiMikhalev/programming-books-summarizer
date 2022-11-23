from pydantic import BaseModel, HttpUrl


class BookBase(BaseModel):
    title: str
    author: str
    cover: HttpUrl | None = None
    summary: str

    class Config:
        schema_extra = {
            'example': {
                'title': 'Fluent Python',
                'author': 'Luciano Ramalho',
                'cover': 'https://learning.oreilly.com/library/cover/9781491946237/250w/',
                'summary': 'Write effective, idiomatic Python code by leveraging its best—and possibly most neglected—features',

            }
        }


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    reader_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    books: list[Book] = []

    class Config:
        orm_mode = True
