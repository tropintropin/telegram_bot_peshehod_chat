from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command

from environs import Env

from lexicon.greeting import greeting


env: Env = Env()
env.read_env('.env')

bot: Bot = Bot(token=env('BOT_TOKEN'), parse_mode='HTML')  # NB! This is token for the test bot!
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer(greeting)


@dp.message()       # for all other messages
async def send_echo(message: Message):
    await message.reply(text='''
Для справки введите или нажмите /help
Нажмите /start, чтобы вернуться в начало''')


if __name__ == '__main__':
    dp.run_polling(bot)

