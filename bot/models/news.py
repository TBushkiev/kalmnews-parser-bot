import datetime
from database.base_class import Base

from sqlalchemy import Column, Integer, String, TIMESTAMP, Float


# no need for __tablename__ because of declarative style (database.base_class)
class News(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    date = Column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)
    sentiment = Column(String, nullable=True)
    score = Column(Float, nullable=True)
