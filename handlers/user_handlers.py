"""Handlers for the basic commands of the bot.
"""

from asyncio import sleep

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

from keyboards.inline_keyboards import create_startup_inline_kb
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
    startup_keyboard = create_startup_inline_kb()
    await message.answer(
        text='<strong>Выберите интересующий вас раздел:</strong>',
        reply_markup=startup_keyboard
    )


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    """
    Handle the command "/help".

    This function processes the "/help" command and sends the help message to the user.

    :param message: The received message object.
    :type message: aiogram.types.Message
    """
    await message.answer(text=LEXICON_RU['/help'])
    startup_keyboard = create_startup_inline_kb()
    await message.answer(
        text='<strong>Выберите интересующий вас раздел:</strong>',
        reply_markup=startup_keyboard
    )


@router.callback_query(F.data == 'help')
async def process_help_press(callback: CallbackQuery):
    """DOCSTRING"""
    if callback.message:
        await callback.message.answer(text=LEXICON_RU['/help'])
        startup_keyboard = create_startup_inline_kb()
        await callback.message.answer(
            text='<strong>Выберите интересующий вас раздел:</strong>',
            reply_markup=startup_keyboard
        )


@router.message(Command(commands='contacts'))
async def process_contacts_command(message: Message):
    """DOCSTRING"""
    # TODO: Change to another answer!
    await message.answer(text=greeting)
    startup_keyboard = create_startup_inline_kb()
    await message.answer(
        text='<strong>Выберите интересующий вас раздел:</strong>',
        reply_markup=startup_keyboard
    )


@router.callback_query(F.data == 'contacts')
async def process_contacts_press(callback: CallbackQuery):
    """DOCSTRING"""
    if callback.message:
        # TODO: Change to another answer!
        await callback.message.answer(text=greeting)
        startup_keyboard = create_startup_inline_kb()
        await callback.message.answer(
            text='<strong>Выберите интересующий вас раздел:</strong>',
            reply_markup=startup_keyboard
        )
