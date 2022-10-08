from flask import Flask, request
from telebot import TeleBot, types
import os
import configparser
config = configparser.ConfigParser()
config.read("settings.ini")
#
#
#
TOKEN = config['DATA']['API_TOKEN']
URL = config['DATA']['URL_HER']
#
#
#
app = Flask(__name__)
bot = TeleBot(TOKEN)

@app.route("/")
def header():
    bot.remove_webhook()
    bot.set_webhook(URL)
    return '!', 200

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет")



if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))