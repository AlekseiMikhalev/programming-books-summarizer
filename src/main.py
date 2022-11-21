from fastapi import FastAPI, status
from pydantic import BaseModel, HttpUrl


class Book(BaseModel):
    title: str
    author: str
    cover: HttpUrl
    key_ideas: str
    tech_stack: set

    class Config:
        schema_extra = {
            'example': {
                'title': 'Fluent Python',
                'author': 'Luciano Ramalho',
                'cover': 'https://learning.oreilly.com/library/cover/9781491946237/250w/',
                'key_ideas': 'Write effective, idiomatic Python code by leveraging its best—and possibly most neglected—features',
                'tech_stack': {'Python'}
            }
        }


class User(BaseModel):  # TODO: move to user sub-app
    username: str
    full_name: str | None = None

    class Config:
        schema_extra = {
            'example': {
                'username': 'aleks_mikhalev',
                'full_name': 'Aleks Mikhalev'
            }
        }


summarizer_app = FastAPI()

fake_books_db = [
    {
        "title": "Fluent Python",
        "author": "Some author",
        "cover": "https://learning.oreilly.com",
        "key_ideas": "Key points of the book",
        "tech_stack": {'python', 'FastAPI', 'AWS'}
    }
]


@summarizer_app.get('/', status_code=status.HTTP_200_OK)
async def root():
    return {
        "application": "Programming Books Summarizer",
        "description": "Application for summarization programming books",
        "author": "Aleksei Mikhalev"
    }


@summarizer_app.get('/books/', response_model=list[Book], status_code=status.HTTP_200_OK)
async def books_list():
    return fake_books_db


@summarizer_app.get('/books/{book_id}', response_model=Book, status_code=status.HTTP_200_OK)
async def book_item(book_id: int):
    result = fake_books_db[book_id]
    return result


@summarizer_app.post('/books/', status_code=status.HTTP_201_CREATED)
async def create_book(book: Book, user: User):
    return book, user


@summarizer_app.put('/books/{book_id}')
async def update_book(book_id: int, book: Book, user: User):
    return {
        'book_id': book_id, **book.dict(),
        'user': user
    }
