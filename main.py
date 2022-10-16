import os
import requests
from flask import Flask, request
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils.executor import start_webhook
import configparser
import db
import button
from aiogram.contrib.fsm_storage.memory import MemoryStorage
config = configparser.ConfigParser()
config.read("settings.ini")
#
TOKEN = config['DATA']['API_TOKEN']
URL = config['DATA']['URL_HER']
URl_TOKEN = config['DATA']['URL_TOKEN']
#
WEBHOOK_SET = config['DATA']['WEBHOOK_SET']
WEBHOOK_PATH = f'/'
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)
#
storage = MemoryStorage()
#
app = Flask(__name__)
bot = Bot(token=TOKEN)
dp= Dispatcher(bot, storage=storage)
async def on_shutdown(dp):
    await bot.delete_webhook()

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
    print(name)
    db.insert_name(name=name, chat_id=message.chat.id)
    await bot.send_message(message.chat.id, f"Запомнил, приветик  {message.text}")
    await state.finish()

@dp.message_handler(commands=['pizza'], state=None)
async def pizza_search(message:types.Message):
    but = types.ReplyKeyboardMarkup(button.button_pizza())
    await bot.send_message(message.chat.id, "Выберите пиццу:", reply_markup=but)
    await button.pizza.pizza_name.set()

@dp.message_handler(state=button.pizza.pizza_name)
async def pizza_size(message: types.Message, state: FSMContext):
    pizn = message.text
    if pizn=="Отмена":
        await bot.send_message(message.chat.id, "Выход", reply_markup=types.ReplyKeyboardRemove())
    elif pizn == "Мясная" and pizn == "Сырная" and pizn == "Веган":
        print(message.text)








if __name__ == '__main__':
    requests.get(url=WEBHOOK_SET)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )