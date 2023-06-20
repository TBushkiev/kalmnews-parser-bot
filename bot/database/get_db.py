from typing import Iterator

from sqlalchemy.orm import sessionmaker

from database.session import SessionLocal


def get_db() -> Iterator[sessionmaker]:
    with SessionLocal() as session:
        with session.begin():
            yield session
