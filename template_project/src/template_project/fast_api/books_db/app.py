from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List


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
    "/authors/", response_model=schema.AuthorInDB, status_code=status.HTTP_201_CREATED
)
def create_author(author: schema.AuthorCreate, db: Session = Depends(get_db)):
    db_author = model.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


@app.get("/authors/", response_model=List[schema.AuthorInDB])
def read_authors(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    authors = db.query(model.Author).offset(skip).limit(limit).all()
    return authors


@app.get("/authors/{author_id}", response_model=schema.AuthorInDB)
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(model.Author).filter(model.Author.id == author_id).first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@app.patch("/authors/{author_id}", response_model=schema.AuthorInDB)
def update_author(
    author_id: int, author_update: schema.AuthorUpdate, db: Session = Depends(get_db)
):
    author = db.query(model.Author).filter(model.Author.id == author_id).first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    for key, value in author_update.dict(exclude_unset=True).items():
        setattr(author, key, value)

    db.commit()
    db.refresh(author)
    return author


@app.delete("/authors/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(model.Author).filter(model.Author.id == author_id).first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(author)
    db.commit()
    return {"detail": "Author deleted successfully"}


@app.post(
    "/books/", response_model=schema.BookInDB, status_code=status.HTTP_201_CREATED
)
def create_book(book: schema.BookCreate, db: Session = Depends(get_db)):
    author = db.query(model.Author).filter(model.Author.id == book.author_id).first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")

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
