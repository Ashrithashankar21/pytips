from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
import bcrypt
from jose import JWTError, jwt
from datetime import datetime, timedelta

import model
import schema
from db_handler import SessionLocal, engine

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0",
    openapi_tags=[
        {"name": "users", "description": "Operations with users."},
        {"name": "token", "description": "Operations with token."},
    ],
    openapi_scheme=[
        {"type": "oauth2", "flows": {"password": {"tokenUrl": "token", "scopes": {}}}}
    ],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/token", response_model=schema.Token, tags=["users"])
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(model.User).filter(model.User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    if not bcrypt.checkpw(
        form_data.password.encode("utf-8"), user.password.encode("utf-8")
    ):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "role": user.role}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(model.User).filter(model.User.email == email).first()
    if user is None:
        raise credentials_exception
    return user


def admin_required(current_user: schema.UserInDB = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")


@app.get("/me", response_model=schema.UserInDB, tags=["users"])
def read_users_me(current_user: schema.UserInDB = Depends(get_current_user)):
    return current_user


auth_router = APIRouter(dependencies=[Depends(get_current_user)])


@auth_router.post(
    "/authors/",
    response_model=schema.AuthorInDB,
    status_code=status.HTTP_201_CREATED,
    tags=["authors"],
)
def create_author(author: schema.AuthorCreate, db: Session = Depends(get_db)):
    db_author = model.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


@auth_router.get("/authors/", response_model=List[schema.AuthorInDB], tags=["authors"])
def read_authors(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
):
    authors = db.query(model.Author).offset(skip).limit(limit).all()
    return authors


@auth_router.get(
    "/authors/{author_id}", response_model=schema.AuthorInDB, tags=["authors"]
)
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(model.Author).filter(model.Author.id == author_id).first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@auth_router.patch(
    "/authors/{author_id}", response_model=schema.AuthorInDB, tags=["authors"]
)
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


@auth_router.delete(
    "/authors/{author_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["authors"]
)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(model.Author).filter(model.Author.id == author_id).first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(author)
    db.commit()
    return {"detail": "Author deleted successfully"}


@auth_router.post(
    "/books/",
    response_model=schema.BookInDB,
    status_code=status.HTTP_201_CREATED,
    tags=["books"],
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


@auth_router.get("/books/", response_model=List[schema.BookInDB], tags=["books"])
def read_books(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
):
    books = db.query(model.Book).offset(skip).limit(limit).all()
    return books


@auth_router.get("/books/{book_id}", response_model=schema.BookInDB, tags=["books"])
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@auth_router.patch(
    "/books/{book_id}",
    response_model=schema.BookInDB,
    tags=["books"],
    dependencies=[Depends(admin_required)],
)
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


@auth_router.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["books"],
    dependencies=[Depends(admin_required)],
)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted successfully"}


app.include_router(auth_router)


@app.post(
    "/register/",
    response_model=schema.UserInDB,
    status_code=status.HTTP_201_CREATED,
    tags=["users"],
)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(model.User).filter(model.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())

    db_user = model.User(
        username=user.username,
        email=user.email,
        password=hashed_password.decode("utf-8"),
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/", response_model=List[schema.UserInDB], tags=["users"])
def read_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    users = db.query(model.User).offset(skip).limit(limit).all()
    return users
