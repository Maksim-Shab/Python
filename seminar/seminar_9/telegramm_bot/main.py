import telebot
from config import token
import random

bot = telebot.TeleBot(token)


"""Команда СТАРТ"""
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.InlineKeyboardButton('Рандомное число')
    item2 = telebot.types.InlineKeyboardButton('Кинуть кость')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Добро пожаловать! ВЫберите нужное миню: ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, как дела?')
    elif message.text == 'Рандомное число':
        bot.send_message(message.chat.id, str(random.randint(1, 10)))
    elif message.text == 'Кинуть кость':
        bot.send_message(message.chat.id, str(random.randint(1, 6)))
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю!')


bot.polling(none_stop=True)