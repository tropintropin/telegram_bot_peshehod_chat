from aiogram import Bot, Dispatcher
from aiogram.types import Message

from environs import Env

env: Env = Env()
env.read_env('.env')

bot: Bot = Bot(token=env('BOT_TOKEN'), parse_mode='HTML')  # NB! This is token for the test bot!
dp: Dispatcher = Dispatcher()


@dp.message()       # for all other messages
async def send_echo(message: Message):
    await message.reply(text="Для справки введите или нажмите /help")


if __name__ == '__main__':
    dp.run_polling(bot)

