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
URl_TOKEN = config['DATA']['URL_TOKEN']
#
#https://api.telegram.org/bot5711773496:AAHyXFloUrGAkN_XAIhSWpfR1_4NZ2l73lk/setWebhook?url=https://tgbot225544.herokuapp.com/
#
app = Flask(__name__)
bot = TeleBot(TOKEN)

@app.route("/")
def header():
    bot.remove_webhook()
    bot.set_webhook(URl_TOKEN)
    return '!', 200
@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет")



if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))