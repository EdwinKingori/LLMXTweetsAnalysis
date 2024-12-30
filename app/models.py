from sqlalchemy import String, Column, Date, Integer
from .database import Base


class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    created_at = Column(Date, nullable=False)
