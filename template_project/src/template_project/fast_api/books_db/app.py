from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session

import model
import schema
from db_handler import (
    SessionLocal,
    engine,
)


model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0",
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(
    "/books/", response_model=schema.BookInDB, status_code=status.HTTP_201_CREATED
)
def create_book(book: schema.BookCreate, db: Session = Depends(get_db)):
    db_book = model.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=list[schema.BookInDB])
def read_books(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
):
    books = db.query(model.Book).offset(skip).limit(limit).all()
    return books


@app.get("/books/{book_id}", response_model=schema.BookInDB)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.patch("/books/{book_id}", response_model=schema.BookInDB)
def update_book(
    book_id: int,
    book_update: schema.BookUpdate,
    db: Session = Depends(get_db),
):
    book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    for key, value in book_update.dict(exclude_unset=True).items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted successfully"}
