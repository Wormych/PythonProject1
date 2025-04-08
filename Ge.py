import telebot

bot = telebot.TeleBot("7396973751:AAF4ThS5i6Kh-73VsxKibAKA2w34qORohks")

@bot.message_handler(commands=["meme"])
def welcome(message):
    bot.send_message(message.chat.id, "Как насчет того, чтобы оторваться вечерком?А ты кто такой?Тромб.")

@bot.message_handler(commands=['photo'])
def stickers(message):
    sti = open('17c026391a54be1a.gif', 'rb')
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(commands=['audio'])
def audio(message):
    music = open('rington.mp3', 'rb')
    bot.send_audio(message.chat.id, music)

@bot.message_handler(commands=['friends'])
def friends(message):
    bot.send_message(message.chat.id, "Your friends:Nick,Bob,John.")

@bot.message_handler(commands=['film'])
def stickers(message):
    sti = open('film.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(commands=['sport'])
def stickers(message):
    sti = open('sport.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(commands=['book'])
def stickers(message):
    sti = open('book.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(commands=['music'])
def audio(message):
    music = open('Rammstein - Ich Will.mp3', 'rb')
    bot.send_audio(message.chat.id, music)

@bot.message_handler(commands=["help"])
def welcome(message):
    bot.send_message(message.chat.id, "/music,/film,/book,/sport,/friends")

bot.polling()