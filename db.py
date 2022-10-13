from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import Bot, types
import configparser
config = configparser.ConfigParser()
config.read("settings.ini")
TOKEN = config['DATA']['API_TOKEN']
bot = Bot(token=TOKEN)
dp= Dispatcher(Bot(TOKEN))

class ADMIN(StatesGroup):
    photo = State()
    name = State()

async def start(message: types.Message):
    await ADMIN.photo.set()
    await bot.send_message(message.chat.id, "Ввод")

async def photo(message: types.Message, state: FSMContext):
    async with state.proxy as data:
        data['photo'] = message.photo[0].file_id
def reg(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'], state=None)
    dp.register_message_handler(photo, content_types=['photo'], state=ADMIN.photo)


