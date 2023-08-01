"""Handlers for the basic commands of the bot.
"""

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.greeting import greeting, instruction
from lexicon.lexicon import LEXICON_RU

from time import sleep


router: Router = Router()


# Handler for the command "/start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(f'{greeting}')
    sleep(2)
    await message.answer(f'{instruction}')
    sleep(2)
    await message.answer('<pre><code>Наш бот находится в разработке, скоро здесь появится новый функционал 🤗</code></pre>')


# Handler for the command "/help"
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
