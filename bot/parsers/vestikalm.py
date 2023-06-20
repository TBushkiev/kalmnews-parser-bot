import datetime
import requests
from bs4 import BeautifulSoup
import locale


class Vesti:
    def __init__(self):
        self.website_link = 'https://vesti-kalmykia.ru/news'

    @staticmethod
    def _get_news_title(html_code) -> str:
        """
        Получает html код страницы, возвращает заголовок новости
        """
        title = html_code.find("h1", class_="item-title uk-margin")
        return title.text.strip()

    @staticmethod
    def _get_news_text(html_code) -> str:
        """
        Получает html код страницы, возвращает текст новости
        """
        text = html_code.find("div", class_="item-text uk-margin")
        if text is None:
            text = html_code.find("h1", class_="item-title uk-margin")
            return str(text)
        return text.text.strip()

    @staticmethod
    def _get_news_date(html_code) -> str:
        """
        Получает html код страницы, возвращает заголовок новости
        """
        news_time: str = html_code.find("div", class_="uk-width-expand@m").find("div", class_="item-date").text
        locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
        date: str = str(datetime.datetime.strptime(news_time, '%d.%m.%Y %H:%M')) # Здесь Python ругался, если нет второго str
        date, time = date.split(',')
        date += ' ' + str(datetime.datetime.now().year)
        date = date + time
        return str(datetime.datetime.strptime(date, u'%d.%m.%Y %H:%M')) # И здесь

    def get_news_data(self, url: str) -> (str, str, str):
        """
        Получает ссылку на новость, возвращает заголовок, текст, дату публикации новости.
        """
        site_response = requests.get(url)
        html_code = BeautifulSoup(site_response.text, "html.parser")

        news_title = self._get_news_title(html_code)
        news_text = self._get_news_text(html_code)
        news_date = self._get_news_date(html_code)
        return news_title, news_text, news_date