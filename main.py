import os
import requests
from flask import Flask, request
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
import configparser
import db
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
bot = Bot(token=TOKEN)
dp= Dispatcher(Bot(TOKEN))
#
async def on_shutdown(dp):
    await bot.delete_webhook()

@dp.message_handler(commands=['start'])
async def startcom(msg: types.Message):
    await bot.send_message(msg.chat.id,"Привет")
@dp.message_handler(commands=['text'])
async def j(db:Dispatcher):
    await db.reg(dp=dp)


if __name__ == '__main__':
    requests.get(url=WEBHOOK_SET)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )