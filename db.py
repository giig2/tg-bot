from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import Bot, types
import configparser
import sqlite3
config = configparser.ConfigParser()
config.read("settings.ini")
TOKEN = config['DATA']['API_TOKEN']
bot = Bot(token=TOKEN)
connect = sqlite3.connect('name.db', check_same_thread=False)
commit = connect.commit()
#dp= Dispatcher(Bot(TOKEN))

class load(StatesGroup):
    name = State()

async def create_table(message):
    try:
        connect.execute("CREATE TABLE `users` (id INTEGER PRIMARY KEY AUTOINCREMENT,chat_id INTEGER,name TEXT)")
    except Exception as a:
        await bot.send_message(message.chat.id, "Таблица не создана. Ошибка")
        print(a)

def select_all_users():
    all = connect.execute("SELECT * FROM `users`")
    print(all)
    print(all.fetchall())
def insert_name(name, chat_id):
    connect.execute("INSERT INTO `users` (`name`, `chat_id`) VALUES (?,?)", (name, chat_id))










