'''Handlers for the "FAQ" section.
'''

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from services.services import get_faq_sections


router: Router = Router()


@router.callback_query(F.text == 'faq')
async def process_faq_press(callback: CallbackQuery):
    """
    Handle the callback query when the "FAQ" button is pressed.

    This function processes the callback query when the "FAQ" button is pressed.
    It sends the sections from the FAQ using an inline keyboard.

    :param callback: The callback query object.
    :type callback: aiogram.types.CallbackQuery
    """
    sections = get_faq_sections()
    # TODO: Create keyboard from list
    await callback.message.answer(
        text='\n\n'.join(sections.keys())
        )


@router.message(Command(commands='faq'))
async def process_faq_command(message: Message):
    """
    Handle the command "/faq".

    This function processes the command "/faq" and sends the sections
    from the FAQ using an inline keyboard.

    :param message: The received message object.
    :type message: aiogram.types.Message
    """
    sections = get_faq_sections()
    # TODO: Create keyboard from list
    await message.answer(
        text='\n\n'.join(sections.keys())
        )
