# schemas.py
from pydantic import BaseModel
from datetime import date


class BookBase(BaseModel):
    title: str
    author_name: str
    release_date: date
    isbn_number: str


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    author_name: str | None = None
    release_date: date | None = None
    isbn_number: str | None = None


class BookInDB(BookBase):
    id: int

    class Config:
        orm_mode = True
