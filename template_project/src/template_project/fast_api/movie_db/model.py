from sqlalchemy import Boolean, Column, Integer, String
from db_handler import Base

class Movies(Base):

    __tablename__ = "movie"
    id = Column(
        Integer, primary_key=True, autoincrement=True, index=True, nullable=False
    )
    movie_id = Column(String, unique=True, index=True, nullable=False)
    movie_name = Column(String(255), index=True, nullable=False)
    director = Column(String(100), index=True, nullable=False)
    geners = Column(String, index=True, nullable=False)
    membership_required = Column(Boolean, nullable=False, default=True)
    cast = Column(String(255), index=True, nullable=False)
    streaming_platform = Column(String, index=True)
