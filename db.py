from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import Bot, types
import configparser
config = configparser.ConfigParser()
config.read("settings.ini")
TOKEN = config['DATA']['API_TOKEN']
bot = Bot(token=TOKEN)
#dp= Dispatcher(Bot(TOKEN))

class load(StatesGroup):
    name = State()



