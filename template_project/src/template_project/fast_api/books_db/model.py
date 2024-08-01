from sqlalchemy import Date, Column, ForeignKey, Integer, String
from db_handler import Base, engine
from sqlalchemy.orm import relationship


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birthdate = Column(Date)
    nationality = Column(String, index=True)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    release_date = Column(Date)
    isbn_number = Column(String, index=True)

    author = relationship("Author", back_populates="books")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="user")
    refresh_token = Column(String, nullable=True)


Base.metadata.create_all(bind=engine)
