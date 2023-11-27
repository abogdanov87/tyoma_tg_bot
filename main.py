import asyncio
import logging

from core.settings import settings
from aiogram import Bot, Dispatcher, executor, types

import core.apps.gpt as gpt


BOT_TOKEN = settings.bots.bot_token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Мяяяяуу!")


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(gpt.get_answer())


if __name__ == '__main__':
    try:
        executor.start_polling(dp)
    finally:
        bot.session.close()
