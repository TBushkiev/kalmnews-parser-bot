import datetime
from crud.news import CRUDNews, crud as crud_news
from telebot import TeleBot
from telebot.types import Message
from parsers.riakalm import parser as riakalm_parser, RiaKalm
from parsers.vestikalm import parser as vestikalm_parser, Vesti
from core.config import settings
from models.news import News
bot = TeleBot(settings.BOT_TOKEN)


def get_data(url: str, parser: RiaKalm | Vesti, crud: CRUDNews) -> (str, str, str):
    title, text, news_date = parser.get_news_data(url=url)

    crud.add_new_item(title=title, text=text, date=news_date)

    return title, text, news_date


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    bot.send_message(chat_id=message.chat.id, text='Привет! Это тестовый бот для мастерской IT-08 по Python')


@bot.message_handler(commands=['add_news'])
def add_news(message: Message):
    params = message.text.split()
    count_words = len(params)
    if count_words > 2 or count_words < 2:
        bot.send_message(chat_id=message.chat.id, text='Вы ввели неверное количество параметров')
    else:
        url = params[1]
        if 'riakalm' in url:
            title, text, news_date = get_data(url=url, parser=riakalm_parser, crud=crud_news)

        elif 'vesti-kalmykia' in url:
            title, text, news_date = get_data(url=url, parser=vestikalm_parser, crud=crud_news)

        bot.send_message(chat_id=message.chat.id, text=f'{title}\n\n{text}\n\n{news_date}')


@bot.message_handler(commands=['get_by_id'])
def get_news_by_id(message: Message):
    params = message.text.split()
    news_id = int(params[1])
    news: News = crud_news.get_by_id(news_id)
    bot.send_message(chat_id=message.chat.id, text=f'{news.title}\n\n{news.text}\n\n{news.date}')


if __name__ == '__main__':
    bot.infinity_polling()
