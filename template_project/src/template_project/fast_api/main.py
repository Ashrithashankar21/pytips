from fastapi import FastAPI, HTTPException, status, Path
from pydantic import BaseModel, Field
from typing import List
from datetime import date

app = FastAPI()


class Book(BaseModel):
    id: int = Field(..., gt=0, example=1)
    title: str = Field(..., min_length=1, max_length=100, example="The Great Gatsby")
    author_name: str = Field(
        ..., min_length=1, max_length=100, example="F. Scott Fitzgerald"
    )
    release_date: date = Field(..., example="1925-04-10")
    isbn_number: str = Field(..., pattern=r"^\d{10}|\d{13}$", example="9780743273565")

    class Config:
        arbitrary_types_allowed = True


books_db: List[Book] = [
    Book(
        id=1,
        title="The Great Gatsby",
        author_name="F. Scott Fitzgerald",
        release_date=date(1925, 4, 10),
        isbn_number="9780743273565",
    ),
]


@app.post("/books/", response_model=Book)
def add_book(book: Book):
    if any(b.id == book.id for b in books_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book with this ID already exists.",
        )
    books_db.append(book)
    return book


@app.get("/books/", response_model=List[Book])
def get_books():
    return books_db


@app.get("/books/{book_id}", response_model=Book)
def get_book(
    book_id: int = Path(..., description="The ID of the book you want to get", gt=0)
):
    book = next((b for b in books_db if b.id == book_id), None)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found."
        )
    return book
