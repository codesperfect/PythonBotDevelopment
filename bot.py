import telebot,os
from telebot import types
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id,"Hello for")

bot.polling()