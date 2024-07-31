from pydantic import BaseModel, EmailStr, constr, validator
from datetime import date
import re


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


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: constr(min_length=8)
    role: str = "user"

    @validator("password")
    def password_complexity(cls, v):
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain at least one special character")
        return v


class UserInDB(UserBase):
    id: int
    role: str  # Add role attribute

    class Config:
        orm_mode = True


class Login(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
