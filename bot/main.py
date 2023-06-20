from telebot import TeleBot
from telebot.types import Message

from core.config import settings

bot = TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    bot.send_message(chat_id=message.chat.id, text='Привет! Это тестовый бот для мастерской IT-08 по Python')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.infinity_polling()
