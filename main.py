from flask import Flask, request
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
import configparser
import logging
config = configparser.ConfigParser()
config.read("settings.ini")
#
#
#
TOKEN = config['DATA']['API_TOKEN']
URL = config['DATA']['URL_HER']
URl_TOKEN = config['DATA']['URL_TOKEN']
#
#https://api.telegram.org/bot5711773496:AAHyXFloUrGAkN_XAIhSWpfR1_4NZ2l73lk/setWebhook?url=https://tgbot5544.herokuapp.com/
#
app = Flask(__name__)
bot = Bot(TOKEN)
dp= Dispatcher(Bot(TOKEN))
async def on_startup(dp):
    await bot.set_webhook(URl_TOKEN, drop_pending_updates=True)
async def on_shutdown(dp):
    await bot.delete_webhook()


@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, "Привет")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=URl_TOKEN,
        kip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown)