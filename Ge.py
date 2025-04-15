import telebot
import random
from telebot import types
import datetime
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs1.log", filemode="a",
                    format="We have next logging message: "
                           "%(asctime)s:%(levelname)s-%(message)s"
                    )
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

bot = telebot.TeleBot("7396973751:AAF4ThS5i6Kh-73VsxKibAKA2w34qORohks")

data = datetime.datetime.now()






@bot.message_handler(commands=["start"])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Яку оцінку сьогодні отримаєш?")
    item2 = types.KeyboardButton("😊 Як справи?")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Hi!".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

def save_message_to_file(user_id, message_text):
    with open("user_messages.txt", "a", encoding="utf-8") as file:
        file.write(f"User {user_id}: {message_text}\n")
        connection = sqlite3.connect("itsteps_DB.sl3", 5)
        cur = connection.cursor()
        # cur.execute("CREATE TABLE MessageBot (data TEXT,message TEXT)")
        cur.execute("INSERT INTO MessageBot (data) VALUES (?)", (data,))
        cur.execute("INSERT INTO MessageBot (message) VALUES (?)", (message_text,))
        connection.commit()
        res = cur.fetchall()
        print(res)
        connection.commit()
        connection.close()

# @bot.message_handler(commands=["meme"])
# def welcome(message):
#     bot.send_message(message.chat.id, "Как насчет того, чтобы оторваться вечерком?А ты кто такой?Тромб.")
#
# @bot.message_handler(commands=['photo'])
# def stickers(message):
#     sti = open('17c026391a54be1a.gif', 'rb')
#     bot.send_sticker(message.chat.id, sti)
#
# @bot.message_handler(commands=['audio'])
# def audio(message):
#     music = open('rington.mp3', 'rb')
#     bot.send_audio(message.chat.id, music)
#
# @bot.message_handler(commands=['friends'])
# def friends(message):
#     bot.send_message(message.chat.id, "Your friends:Nick,Bob,John.")
#
# @bot.message_handler(commands=['film'])
# def stickers(message):
#     sti = open('film.jpg', 'rb')
#     bot.send_sticker(message.chat.id, sti)
#
# @bot.message_handler(commands=['sport'])
# def stickers(message):
#     sti = open('sport.jpg', 'rb')
#     bot.send_sticker(message.chat.id, sti)
#
# @bot.message_handler(commands=['book'])
# def stickers(message):
#     sti = open('book.jpg', 'rb')
#     bot.send_sticker(message.chat.id, sti)
#
# @bot.message_handler(commands=['music'])
# def audio(message):
#     music = open('Rammstein - Ich Will.mp3', 'rb')
#     bot.send_audio(message.chat.id, music)
#
# @bot.message_handler(commands=["help"])
# def welcome(message):
#     bot.send_message(message.chat.id, "/music,/film,/book,/sport,/friends")

@bot.message_handler(content_types=['text'])
def processing_text(message):
    save_message_to_file(message.from_user.id, message.text)
    if message.text == "🎲 Яку оцінку сьогодні отримаєш?":
        bot.send_message(message.chat.id, random.randint(2,12))
    elif message.text  == "😊 Як справи?":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Нормально", callback_data='good')
        item2 = types.InlineKeyboardButton("Плохо", callback_data='bad')
        item3 = types.InlineKeyboardButton("Возможно", callback_data='4t')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Чудово! Помив підлогу?".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

    elif message.text  == "Привіт":
        bot.send_message(message.chat.id, "Здоров")
    elif message.text == "чіназес":
        bot.send_message(message.chat.id, "саунтрес")
    else:
        bot.send_message(message.chat.id, "Я не зрозумів тебе")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'От і добре ')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                    text="Cool!!!!!")
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Your nigodyai')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                    text="Run!!!!")

            elif call.data == '4t':
                bot.send_message(call.message.chat.id, 'Clear floor')
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                    text="Okay")

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="😊 Як справи?", reply_markup=None)

            # show alert
    except Exception as e:
        print(repr(e))
bot.polling()