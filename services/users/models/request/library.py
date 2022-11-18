from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from library.models.data.library import Classification


class BookReq(BaseModel):
    book_id: int
    title: str
    classification: Classification
    author: str
    year_published: datetime
    edition: int


class BookDetails(BaseModel):
    title: Optional[str] = None
    classification: Optional[Classification] = None
    author: Optional[str] = None
    year_published: Optional[datetime] = None
    edition: Optional[int] = None
