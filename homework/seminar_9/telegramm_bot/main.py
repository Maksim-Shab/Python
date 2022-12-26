import telebot
from config import token
from anecdote import anekdot

bot = telebot.TeleBot(token)

"""Команда СТАРТ"""
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.InlineKeyboardButton('Калькулятор')
    item2 = telebot.types.InlineKeyboardButton('Анекдот')
    
    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужное миню: ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Анекдот':
        bot.send_message(message.chat.id, str(anekdot()))
    elif message.text == 'Калькулятор':
        bot.send_message(message.chat.id, 'Введите пример в формате "x+y"')
    elif str(message.text).__contains__('+'):
        bot.send_message(message.chat.id, f'Ответ равен: {calc_variables(str(message.text), "+")}')
    elif str(message.text).__contains__('-'):
        bot.send_message(message.chat.id, f'Ответ равен: {calc_variables(str(message.text), "-")}')
    elif str(message.text).__contains__('*'):
        bot.send_message(message.chat.id, f'Ответ равен: {calc_variables(str(message.text), "*")}')
    elif str(message.text).__contains__('×'):
        bot.send_message(message.chat.id, f'Ответ равен: {calc_variables(str(message.text), "×")}')
    elif str(message.text).__contains__('/'):
        bot.send_message(message.chat.id, f'Ответ равен: {calc_variables(str(message.text), "/")}')
    else:
        bot.send_message(message.chat.id, 'Введенны не корректные данные')

def calc_variables(data, symbol):
    x = data.split(symbol)[0]
    y = data.split(symbol)[1]
    return calc_result(int(x), int(y), symbol)
   

def calc_result(x, y, symbol):
    if symbol == '+':
        return x + y
    elif symbol == '-':
        return x - y
    elif symbol == '*':
        return x * y    
    elif symbol == '×':
        return x * y    
    elif symbol == '/':
        return x / y


bot.polling(none_stop=True)