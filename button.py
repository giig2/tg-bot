from aiogram import types
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import configparser
storage = MemoryStorage()
config = configparser.ConfigParser()
config.read("settings.ini")
TOKEN = config['DATA']['API_TOKEN']
bot = Bot(token=TOKEN)
dp= Dispatcher(bot, storage=storage)

def button_pizza():
    but = types.ReplyKeyboardMarkup()
    but1 = types.KeyboardButton("Мясная")
    but2 = types.KeyboardButton("Сырная")
    but3 = types.KeyboardButton("Веган")
    but = but.add(but1, but2, but3)
    return but
