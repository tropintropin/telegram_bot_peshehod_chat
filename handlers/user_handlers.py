"""Handlers for the basic commands of the bot.
"""

from asyncio import sleep

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.greeting import greeting, instruction
from lexicon.lexicon import LEXICON_RU


router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    """
    Handle the command "/start".

    This function processes the "/start" command when the user starts interacting with the bot.
    It sends a greeting message, an instruction message, and a message about the bot being in development.

    :param message: The received message object.
    :type message: aiogram.types.Message
    """
    await message.answer(f'{greeting}')
    await sleep(2)
    await message.answer(f'{instruction}')
    await sleep(2)
    # TODO: Change the message & docstring for this answer when production:
    await message.answer('<pre><code>Наш бот находится в разработке, скоро здесь появится новый функционал 🤗</code></pre>')


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    """
    Handle the command "/help".

    This function processes the "/help" command and sends the help message to the user.

    :param message: The received message object.
    :type message: aiogram.types.Message
    """
    await message.answer(text=LEXICON_RU['/help'])
