import telebot
from config import token
import random

bot = telebot.TeleBot(token)


"""Команда СТАРТ"""
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.InlineKeyboardButton('Жми сюда!')
    item2 = telebot.types.InlineKeyboardButton('Отгадай число')
    item3 = telebot.types.InlineKeyboardButton('Знак задиака')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Добро пожаловать! ВЫберите нужное миню: ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):

      
    if message.text == 'Отгадай число':
        msg = bot.send_message(message.chat.id, 'Я загадал число от 1 до 10, отгадай его')
        bot.register_next_step_handler(msg, num_rnd)
   
    elif message.text == 'Знак задиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1 = telebot.types.InlineKeyboardButton('Овен', callback_data = 1)
        item2 = telebot.types.InlineKeyboardButton('Телец', callback_data = 2)
        item3 = telebot.types.InlineKeyboardButton('Близнецы', callback_data = 3)
        item4 = telebot.types.InlineKeyboardButton('Рак', callback_data = 4)
        item5 = telebot.types.InlineKeyboardButton('Лев', callback_data = 5)
        item6 = telebot.types.InlineKeyboardButton('Дева', callback_data = 6)
        item7 = telebot.types.InlineKeyboardButton('Весы', callback_data = 7)
        item8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data = 8)
        item9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data = 9)
        item10 = telebot.types.InlineKeyboardButton('Козерог', callback_data = 10)
        item11 = telebot.types.InlineKeyboardButton('Водолей', callback_data = 11)
        item12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data = 12)
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        bot.send_message(message.chat.id, 'Отлично, выбери свой знак задиака', reply_markup = markup)
   
    elif message.text == 'Жми сюда!':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG73Vjo1mRgC9-dIS5kUjjdMG09qeodAACXwEAAhAabSLLoLkqsC4-oywE')

    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю!')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '1':
        bot.send_message(call.message.chat.id, 'Овен – импульсивный и независимый. Смел, уверен в себе и энергичен, проявляет невероятное упорство в достижении целей и колоссальное трудолюбие. Острый ум и сильная воля делают этот знак одним из самых ярких, однако ладить с Овнами весьма непросто.')
    if call.data == '2':
        bot.send_message(call.message.chat.id, 'Телец – талантливый и трудолюбивый. Этот знак отличает постоянство и стремление к комфорту, а также запасливость, расчетливость и практичность. Тельцы настоящие коллекционеры, причем не только материальных ценностей, но и жизненного опыта.')
    if call.data == '3':
        bot.send_message(call.message.chat.id, 'Лев – харизматичный и притягательный. Он открыт, дружелюбен и силен, может с легкостью повести за собой людей, поэтому имеет много друзей и почитателей. От своего окружения требует безоговорочного подчинения и преданности, очень ценит крепкую дружбу и всегда готов придти на помощь.')
    if call.data == '4':
        bot.send_message(call.message.chat.id, 'Рак – чувствительный и проницательный. Эмоциональное состояние этого знака напрямую зависит от взаимоотношений с окружающими людьми и часто меняется. Смена настроений приводит к тому, что Раки переходят от активной деятельности к пассивному состоянию. Однако отличная интуиция и внимание к мелочам помогают им выйти из самых сложных ситуаций.')
    if call.data == '5':
        bot.send_message(call.message.chat.id, 'Близнецы – любознательны и контактны. Могут обрабатывать огромное количество информации, постоянно пополняя копилку своих знаний. Имеют развитый интеллект, нестандартное мышление и огромное количество друзей и знакомых.')
    if call.data == '6':
        bot.send_message(call.message.chat.id, 'Дева – чувственная и ранимая. Дева отлично приспосабливается к обстоятельствам, обладает безграничным терпением и поразительной работоспособностью. Аккуратные и педантичные Девы выполняют любое дело неторопливо и основательно, предъявляя высокие требования к себе и окружающим.')
    if call.data == '7':
        bot.send_message(call.message.chat.id, 'Весы – уравновешены и дипломатичны. Редко проявляют эмоции, оставляя все переживания внутри, и стараются поддерживать со всеми хорошие отношения. Они влюбчивы и эстетичны, тонко чувствуют красоту окружающего мира, нетерпимы к грубости и дурному вкусу.')
    if call.data == '8':
        bot.send_message(call.message.chat.id, 'Скорпион – мужественный и стойкий. Бури страстей, одолевающие этот знак, не всегда находятся под контролем. Скорпионам свойственны страстные увлечения, отчаянная ревность и даже агрессия. Однако в большинстве случаев эти эмоции не выходят наружу, а остаются внутри, провоцируя глубокие переживания.')
    if call.data == '9':
        bot.send_message(call.message.chat.id, 'Стрелец - мечтательный и бесстрашный. Стрелец - путешественник и первооткрыватель, он отличается любознательностью и жаждой знаний, однако порой вспыльчив и чересчур эмоционален.')
    if call.data == '10':
        bot.send_message(call.message.chat.id, 'Козерог – надежный и прагматичный. Организаторские способности Козерогов, а также умение планировать возносят их на самый верх социальной пирамиды. Талантливые руководители и прирожденные лидеры, Козероги все держат под контролем и могут справиться с любой ситуацией.')
    if call.data == '11':
        bot.send_message(call.message.chat.id, 'Водолей – свободолюбивый и эксцентричный. Всегда настаивает на своей правоте и имеет обо всем свое суждение. Необычный и независимый Водолей всегда идет по своему пути, не обращая внимания на установленные в обществе правила. Бунтарский характер этого знака уравновешивается обостренным чувством справедливости и безграничной честностью.')
    if call.data == '12':
        bot.send_message(call.message.chat.id, 'Рыбы – изменчивые и непрактичные. Хорошо развитое воображение и богатый внутренний мир часто уводят Рыб в страну грез. Фантазии и мечты настолько заполняют жизнь, что порой этому знаку очень трудно адаптироваться к реальному миру. Рыбы умеют сочувствовать и сопереживать, они всегда утешат в трудную минуту и помогут нуждающимся.')

def num_rnd(message):
    x = random.randint(0, 10)
    if message.text == str(x):
        bot.send_message(message.chat.id, 'Угадал')
    else:
        bot.send_message(message.chat.id, 'Не Угадал')

bot.polling(none_stop=True)