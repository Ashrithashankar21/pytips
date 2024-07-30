# schemas.py
from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class AuthorBase(BaseModel):
    name: str
    birthdate: date
    nationality: str


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(BaseModel):
    name: str | None = None
    birthdate: date | None = None
    nationality: str | None = None


class AuthorInDB(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    author_id: int
    release_date: date
    isbn_number: str


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    author_id: int | None = None
    release_date: date | None = None
    isbn_number: str | None = None


class BookInDB(BookBase):
    id: int
    author: AuthorInDB

    class Config:
        orm_mode = True
