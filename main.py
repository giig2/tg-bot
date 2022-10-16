import os
import requests
from flask import Flask, request
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils.executor import start_webhook
import configparser
import db
from aiogram.contrib.fsm_storage.memory import MemoryStorage
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
storage = MemoryStorage()
app = Flask(__name__)
bot = Bot(token=TOKEN)
dp= Dispatcher(bot, storage=storage)
#
async def on_shutdown(dp):
    await bot.delete_webhook()
#
#

@dp.message_handler(commands=['start'])
async def startcom(msg: types.Message):
    print(1)
    await bot.send_message(msg.chat.id,"Привет")

@dp.message_handler(commands=['load'])
async def lod(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, "Напиши слово")
    await db.load.name.set()

@dp.message_handler(state=db.load.name)
async def lod_name(message: types.Message, state: FSMContext):
    name = message.text
    current_state = await state.get_state()
    print(name)
    print(current_state)
    await bot.send_message(message.chat.id, message.text)
    await state.finish()



if __name__ == '__main__':
    requests.get(url=WEBHOOK_SET)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )