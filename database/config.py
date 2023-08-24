"""Config sqlalchemy resources."""
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from database.settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER

DATABASE_URL = URL.create(
    'postgresql',
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME,
    port=DB_PORT,
)

engine = create_engine(DATABASE_URL, echo=True)

db_session = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
    ),
)

Base = declarative_base()
