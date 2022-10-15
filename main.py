import os
import requests
from flask import Flask, request
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils.executor import start_webhook
import configparser
import db
from aiogram.dispatcher.filters.state import State
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
# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)
print(TOKEN)
#https://api.telegram.org/bot5657857094:AAGsQA1cqAv6CoF390JAmQp4qc9IM1CS-10/getWebhookInfo
#https://api.telegram.org/bot5657857094:AAGsQA1cqAv6CoF390JAmQp4qc9IM1CS-10/setWebhook?url=https://ggggbot4.herokuapp.com/
#
app = Flask(__name__)
bot = Bot(token=TOKEN)
dp= Dispatcher(Bot(TOKEN))
#
async def on_shutdown(dp):
    await bot.delete_webhook()
#
#

@dp.message_handler(commands=['start'])
async def startcom(msg: types.Message):
    print(1)
    await bot.send_message(msg.chat.id,"Привет")

db.reg(dp=dp)




if __name__ == '__main__':
    requests.get(url=WEBHOOK_SET)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )