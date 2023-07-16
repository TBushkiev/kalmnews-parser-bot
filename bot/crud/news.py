from typing import Type

from sqlalchemy import select

from database.get_db import get_db
from models.news import News


class CRUDNews:
    def __init__(self, model: Type[News]):
        self.model = model

    @staticmethod
    def add_new_item(title, text, date, sentiment=None, score=None):
        session = get_db()
        news = News(title=title, text=text, date=date, sentiment=sentiment, score=score)
        session.add(news)
        session.commit()

    def get_by_id(self, news_id):
        session = get_db()
        query = select(self.model).where(self.model.id == news_id)
        return session.execute(query).scalar()


crud = CRUDNews(News)
