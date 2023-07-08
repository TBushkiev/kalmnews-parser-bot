from sqlalchemy import create_engine, URL
from sqlalchemy.orm import Session, sessionmaker

from core.config import settings
from database.base import *

# https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
# turn on 'echo=True' only for testing purposes


SQLALCHEMY_DATABASE_URL = URL.create(
    drivername='postgresql+psycopg2',
    username=settings.DB_USERNAME,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=Session)


def init_models() -> None:
    # create db tables
    Base.metadata.create_all(engine)

init_models()
