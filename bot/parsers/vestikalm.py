import datetime
import requests
from bs4 import BeautifulSoup


class Vesti:
    month_dict = {
        'января': '1',
        'февраля': '2',
        'марта': '3',
        'апреля': '4',
        'мая': '5',
        'июня': '6',
        'июля': '7',
        'августа': '8',
        'сентября': '9',
        'октября': '10',
        'ноября': '11',
        'декабря': '12'
    }

    def __init__(self):
        self.website_link = 'https://vesti-kalmykia.ru/news'

    @staticmethod
    def _get_news_title(html_code) -> str:
        """
        Получает html код страницы, возвращает заголовок новости
        """
        title = html_code.find("h1", class_="item-title uk-margin")
        return title.text.strip().replace('\xa0', ' ')

    @staticmethod
    def _get_news_text(html_code) -> str:
        """
        Получает html код страницы, возвращает текст новости
        """
        text = html_code.find("div", class_="item-text uk-margin")
        if text is None:
            text = html_code.find("h1", class_="item-title uk-margin")
            return str(text)
        return text.text.strip().replace('\xa0', ' ')

    @staticmethod
    def _get_news_date(html_code) -> str:
        """
        Получает html код страницы, возвращает заголовок новости
        """
        news_time: str = html_code.find("div", class_="uk-width-expand@m").find("div", class_="item-date").text

        date, time = news_time.split(', ')

        date = date.split()
        date[1] = Vesti.month_dict[date[1]]
        if len(date) == 2:
            date.append(str(datetime.datetime.now().year))

        date = ' '.join(date)
        news_time = ', '.join([date, time])
        return str(datetime.datetime.strptime(news_time, '%d %m %Y, %H:%M'))

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


if __name__ == '__main__':
    url = 'https://vesti-kalmykia.ru/news/zaversheno-rassledovanie-ugolovnogo-dela-v-otnoshenii-sotrudnika-celinnogo-res-obvinyaemogo-v-zloupotreblenii-sluzhebnymi-polnomochiyami'  # новость из текущего года
    old_news_url = 'https://vesti-kalmykia.ru/news/v-zagorodnoj-rezidencii-basana-gorodovikova-sostoyalas-uborka'  # новость из прошлого года

    parser = Vesti()
    print(parser.get_news_data(url=url))
    print(parser.get_news_data(url=old_news_url))
