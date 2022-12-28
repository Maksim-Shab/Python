import telebot
from config import token
import random

bot = telebot.TeleBot(token)

def comrpes(messeg):
    str = messeg.text[0]
    bot.send_message(messeg.chat.id, str)
    bot.send_sticker(messeg.chat.id, 'CAACAgIAAxkBAAEG73Vjo1mRgC9-dIS5kUjjdMG09qeodAACXwEAAhAabSLLoLkqsC4-oywE')
    bot.send_message(messeg.chat.id, 'для повторного сжатия снова нажмите на кнопку "Сжать"')

"""Команда СТАРТ"""
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.InlineKeyboardButton('Рандомное число')
    item2 = telebot.types.InlineKeyboardButton('Кинуть кость')
    item3 = telebot.types.InlineKeyboardButton('Как дела?')
    item4 = telebot.types.InlineKeyboardButton('Cжать')
    item5 = telebot.types.InlineKeyboardButton('Загадай число')
    item6 = telebot.types.InlineKeyboardButton('Знак задиака')

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, 'Добро пожаловать! ВЫберите нужное миню: ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, как дела?')
   
    elif message.text == 'Рандомное число':
        bot.send_message(message.chat.id, str(random.randint(1, 10)))
   
    elif message.text == 'Как дела?':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1 = telebot.types.InlineKeyboardButton('Не очень', callback_data = 1)
        item2 = telebot.types.InlineKeyboardButton('Хорошо', callback_data = 2)
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Отлично, а у вас?', reply_markup = markup)
   
    elif message.text == 'Кинуть кость':
        bot.send_message(message.chat.id, str(random.randint(1, 6)))
    
    elif message.text == 'Cжать':
        mesg = bot.send_message(message.chat.id, 'Введите строку которую хотите сжать')
        bot.register_next_step_handler(mesg, comrpes)

    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю!')



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '1':
        bot.send_message(call.message.chat.id, 'Почему?')
    if call.data == '2':
        bot.send_message(call.message.chat.id, 'Я рад!')

bot.polling(none_stop=True)