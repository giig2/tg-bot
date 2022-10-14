import os
import requests
from flask import Flask, request
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

@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=URl_TOKEN)
    return '!', 200



if __name__ == '__main__':
    #requests.get(WEBHOOK_SET)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', default=5000)))

