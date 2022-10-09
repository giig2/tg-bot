import os
from flask import Flask, request
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
import configparser
config = configparser.ConfigParser()
config.read("settings.ini")
#
#
#
TOKEN = config['DATA']['API_TOKEN']
WEBHOOK_HOST = config['DATA']['URL_HER']
URl_TOKEN = config['DATA']['URL_TOKEN']
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')
WEBHOOK_PATH = f'/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)
print(TOKEN)
#
#https://api.telegram.org/bot5657857094:AAGsQA1cqAv6CoF390JAmQp4qc9IM1CS-10/setWebhook?url=https://tgbot5544.herokuapp.com/
#
app = Flask(__name__)
bot = Bot(token=TOKEN)
dp= Dispatcher(Bot(TOKEN))
async def on_shutdown(dp):
    await bot.delete_webhook()


@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, "Привет")


if __name__ == '__main__':
    start_webhook(
        start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            skip_updates=True,
            on_shutdown=on_shutdown,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )
    )