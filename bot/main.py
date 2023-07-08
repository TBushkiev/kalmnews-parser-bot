import datetime
from crud.news import crud
from telebot import TeleBot
from telebot.types import Message
from parsers.riakalm import parser as riakalm_parser
from parsers.vestikalm import parser as vestikalm_parser
from core.config import settings

bot = TeleBot(settings.BOT_TOKEN)


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
            title, text, news_date = riakalm_parser.get_news_data(url=url)

            crud.add_new_item(title=title, text=text, date=news_date)

            bot.send_message(chat_id=message.chat.id, text=f'{title}\n{text}\n{news_date}')

            bot.send_message(chat_id=message.chat.id, text=f'{title}\n{text}\n{news_date}')
        elif 'vesti-kalmykia' in url:
            title, text, news_date = vestikalm_parser.get_news_data(url=url)

            crud.add_new_item(title=title, text=text, date=news_date)

            bot.send_message(chat_id=message.chat.id, text=f'{title}\n{text}\n{news_date}')


if __name__ == '__main__':
    bot.infinity_polling()
