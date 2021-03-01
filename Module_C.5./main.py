import telebot

TOKEN = "1694018350:AAH0-VBbzxwrDz9GrE2TmoOC4CwlbT8gdDs"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f"Welcome, {message.chat.username}")

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

@bot.message_handler(content_types=['text', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice to meet you XDD')

bot.polling(none_stop=True)