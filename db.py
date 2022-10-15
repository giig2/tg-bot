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

async def lod(message: types.Message, state: FSMContext):
        await bot.send_message(message.chat.id, "Напиши слово")
        await load.name.state
        await print(state)

async def lod_name(message: types.Message, state: FSMContext):
    print(state)
    print(message.text)

def reg(dp: Dispatcher):
    dp.register_message_handler(lod, commands=['load'], )
    dp.register_message_handler(lod_name, state=load.name)





