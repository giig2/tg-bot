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
    requests.get(WEBHOOK_SET)
    bot.run_webhooks(listen="0.0.0.0",
                     port=os.getenv('PORT'),
                     webhook_url=URL,)


import os
import telebot
from flask import Flask, request

TOKEN = '1810242195:AAFfImqq9mPT81rs3ApL74eUob5u8A9oxb8'
APP_URL = f'https://vitaljaheroku.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo(message):
    bot.reply_to(message, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))