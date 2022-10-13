import os
import requests
from flask import Flask
import configparser
from telebot import TeleBot, types
config = configparser.ConfigParser()
config.read("settings.ini")
#
#
#
TOKEN = config['DATA']['API_TOKEN']
URL = config['DATA']['URL_HER']
URl_TOKEN = config['DATA']['URL_TOKEN']
WEBHOOK_SET = config['DATA']['WEBHOOK_SET']
WEBHOOK_PATH = f'/'
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)
print(TOKEN)
#
#
#
app = Flask(__name__)
bot = TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет")



if __name__ == '__main__':
    app.run()
    requests.get(WEBHOOK_SET)