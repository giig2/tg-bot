from aiogram import types
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import configparser
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
storage = MemoryStorage()
config = configparser.ConfigParser()
config.read("settings.ini")
TOKEN = config['DATA']['API_TOKEN']
bot = Bot(token=TOKEN)
dp= Dispatcher(bot, storage=storage)

class pizza(StatesGroup):
    pizza_name = State()
    size = State()
    count = State()

pizza_n = ["Мясная", "Сырная", "Веган"]
def mmm():
    for i in pizza_n:
        print(i)

def button_pizza():
    but_all=[[
        types.KeyboardButton("Мясная"),
        types.KeyboardButton("Сырная"),
        types.KeyboardButton("Веган"),
        types.KeyboardButton("Отмена")
    ]]
    return but_all
