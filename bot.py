from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from environs import Env


env: Env = Env()
env.read_env('.env')

bot: Bot = Bot(env('BOT_TOKEN'))
dp: Dispatcher = Dispatcher()


@dp.message()
async def send_echo(message: Message):
    await message.reply(text=r"Я ещё маленький бот, но скоро вырасту и научусь вам помогать. А пока предлагаю вам сайт Пешеход Тура: https://peshehodtour.ru")


if __name__ == '__main__':
    dp.run_polling(bot)
