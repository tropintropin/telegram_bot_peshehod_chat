from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove

from environs import Env

env: Env = Env()
env.read_env('.env')

bot: Bot = Bot(env('BOT_TOKEN'))  # NB! This is token for the test bot!
dp: Dispatcher = Dispatcher()


@dp.message()       # for all other messages
async def send_echo(message: Message):
    await message.reply(text=r"Для справки введите или нажмите /help")


if __name__ == '__main__':
    dp.run_polling(bot)
