import datetime
import requests
from bs4 import BeautifulSoup


class RiaKalm:
    def __init__(self):
        self.website_link = 'https://riakalm.ru/'

    @staticmethod
    def _get_news_title(html_code) -> str:
        """
        Получает html код страницы, возвращает заголовок новости
        """
        tag_h2 = html_code.find("h2", itemprop="name")
        return tag_h2.text.strip()

    @staticmethod
    def _get_news_text(html_code) -> str:
        """
        Получает html код страницы, возвращает текст новости
        """
        tag_meta = html_code.find('meta', property='og:description')
        news_text: str = tag_meta.get('content')
        news_text = news_text.strip().replace('\xa0', ' ').replace('\n\n', ' ')

        redundant_index = news_text.find('{')
        return news_text[:redundant_index].strip()

    @staticmethod
    def _get_news_date(html_code) -> str:
        """
        Получает html код страницы, возвращает заголовок новости
        """
        news_time: str = html_code.find("time", itemprop="datePublished").text
        return str(datetime.datetime.strptime(news_time, '%H:%M %d.%m.%Y'))

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
