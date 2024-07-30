from sqlalchemy import Date, Column, Integer, String
from db_handler import Base, engine


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_name = Column(String, index=True)
    release_date = Column(Date)
    isbn_number = Column(String, index=True)


Base.metadata.create_all(bind=engine)
