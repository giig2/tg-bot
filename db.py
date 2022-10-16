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

 #def create_table(self, chat_id):
        #self.connect.execute(f"CREATE TABLE {chat_id}(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT)")
def select_all_users():
    all = connect.execute("SELECT * FROM `users`")
    return all.fetchall()
def insert_name(name):
    connect.execute("INSERT INTO `users` VALUES name=?", (name))










