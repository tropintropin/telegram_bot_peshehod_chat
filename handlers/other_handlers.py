from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message(StateFilter(default_state))
async def send_echo(message: Message):
    """
    Handle the received message and send a copy back to the sender.

    This function is an echo bot that sends a copy of the received message back to the sender.
    It uses the 'send_copy' method of the 'message' object to send the same message.

    :param message: The received message object to be echoed back.
    :type message: aiogram.types.Message
    """
    try:
        await message.send_copy(chat_id=message.chat.id)  # TODO: Delete this before relise!
    except:
        await message.reply(text=LEXICON_RU['no_echo'])  # TODO: Write good no_echo reply

