from typing import Type
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


crud = CRUDNews(News)
