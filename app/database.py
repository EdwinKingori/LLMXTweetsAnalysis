from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

# # syntax
# SQLALCHEMY_DATABASE_URL  = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


# an Engine, which the Session will use for connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# creating a SessionLocal class to communicate with the sql database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# base class for models
Base = declarative_base()


# a dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
