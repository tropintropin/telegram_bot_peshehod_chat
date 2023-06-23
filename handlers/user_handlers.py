from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from lexicon.greeting import greeting, instruction

from time import sleep


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(f'{greeting}')
    sleep(2)
    await message.answer(f'{instruction}')
    sleep(2)
    await message.answer('<pre><code>Наш бот находится в разработке, скоро здесь появится новый функционал 🤗</code></pre>')


@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text='''
Для справки введите или нажмите /help
Нажмите /start, чтобы вернуться в начало''')