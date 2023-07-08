from sqlalchemy.orm import Session

from database.session import SessionLocal


def get_db() -> Session:
    return SessionLocal()
