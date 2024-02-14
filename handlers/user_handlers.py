"""Handlers for the basic commands of the bot.
"""

from typing import Any, Dict

from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message

from keyboards.inline_keyboards import (
    create_bonus_inline_kb,
    create_feedback_inline_kb,
    create_startup_inline_kb,
    create_stickers_inline_kb,
)
from lexicon.greeting import greeting, instruction
from lexicon.lexicon import LEXICON_RU
from services.services import get_faq_sections

router: Router = Router()


@router.message(CommandStart(), StateFilter(default_state))
@router.message(CommandStart(), ~StateFilter(default_state))
async def process_start_command(message: Message):
    """
    Handle the command "/start".

    This function processes the "/start" command when the user
    starts interacting with the bot.

    It sends a greeting message, an instruction message,
    and a message about the bot being in development.

    :param message: The received message object.
    :type message: aiogram.types.Message
    """
    await message.answer(f"{greeting}")
    await message.answer(f"{instruction}")
    startup_keyboard = create_startup_inline_kb()
    await message.answer(
        text="<strong>Выберите интересующий вас раздел:</strong>",
        reply_markup=startup_keyboard,
    )

    stikers_keyboard = create_stickers_inline_kb()
    await message.answer(text=LEXICON_RU["stickers"], reply_markup=stikers_keyboard)
    bonus_keyboard = create_bonus_inline_kb()
    await message.answer(text=LEXICON_RU["bonus"], reply_markup=bonus_keyboard)


@router.message(Command(commands="cancel"), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(text=LEXICON_RU["/cancel"])
    await message.answer(text=LEXICON_RU["/help"])
    startup_keyboard = create_startup_inline_kb()
    await message.answer(
        text="<strong>Выберите интересующий вас раздел:</strong>",
        reply_markup=startup_keyboard,
    )

    stikers_keyboard = create_stickers_inline_kb()
    await message.answer(text=LEXICON_RU["stickers"], reply_markup=stikers_keyboard)
    bonus_keyboard = create_bonus_inline_kb()
    await message.answer(text=LEXICON_RU["bonus"], reply_markup=bonus_keyboard)


@router.callback_query(F.data == "cancel", StateFilter(default_state))
async def process_cancel_press(callback: CallbackQuery):
    if callback.message:
        await callback.message.answer(text=LEXICON_RU["/cancel"])
        await callback.message.answer(text=LEXICON_RU["/help"])
        startup_keyboard = create_startup_inline_kb()
        await callback.message.answer(
            text="<strong>Выберите интересующий вас раздел:</strong>",
            reply_markup=startup_keyboard,
        )

        stikers_keyboard = create_stickers_inline_kb()
        await callback.message.answer(
            text=LEXICON_RU["stickers"], reply_markup=stikers_keyboard
        )
        bonus_keyboard = create_bonus_inline_kb()
        await callback.message.answer(
            text=LEXICON_RU["bonus"], reply_markup=bonus_keyboard
        )


@router.message(Command(commands="help"))
async def process_help_command(message: Message):
    """
    Handle the command "/help".

    This function processes the "/help" command
    and sends the help message to the user.

    :param message: The received message object.
    :type message: aiogram.types.Message
    """
    await message.answer(text=LEXICON_RU["/help"])
    startup_keyboard = create_startup_inline_kb()
    await message.answer(
        text="<strong>Выберите интересующий вас раздел:</strong>",
        reply_markup=startup_keyboard,
    )

    stikers_keyboard = create_stickers_inline_kb()
    await message.answer(text=LEXICON_RU["stickers"], reply_markup=stikers_keyboard)
    bonus_keyboard = create_bonus_inline_kb()
    await message.answer(text=LEXICON_RU["bonus"], reply_markup=bonus_keyboard)


@router.callback_query(F.data == "help")
async def process_help_press(callback: CallbackQuery):
    if callback.message:
        await callback.message.answer(text=LEXICON_RU["/help"])
        startup_keyboard = create_startup_inline_kb()
        await callback.message.answer(
            text="<strong>Выберите интересующий вас раздел:</strong>",
            reply_markup=startup_keyboard,
        )

        stikers_keyboard = create_stickers_inline_kb()
        await callback.message.answer(
            text=LEXICON_RU["stickers"], reply_markup=stikers_keyboard
        )
        bonus_keyboard = create_bonus_inline_kb()
        await callback.message.answer(
            text=LEXICON_RU["bonus"], reply_markup=bonus_keyboard
        )


@router.message(Command(commands="contacts"))
async def process_contacts_command(message: Message):
    """DOCSTRING"""
    await message.answer(text=greeting)
    startup_keyboard = create_startup_inline_kb()
    await message.answer(
        text="<strong>Выберите интересующий вас раздел:</strong>",
        reply_markup=startup_keyboard,
    )

    stikers_keyboard = create_stickers_inline_kb()
    await message.answer(text=LEXICON_RU["stickers"], reply_markup=stikers_keyboard)
    bonus_keyboard = create_bonus_inline_kb()
    await message.answer(text=LEXICON_RU["bonus"], reply_markup=bonus_keyboard)


@router.callback_query(F.data == "contacts")
async def process_contacts_press(callback: CallbackQuery):
    """DOCSTRING"""
    if callback.message:
        # TODO: Change to another answer!
        await callback.message.answer(text=greeting)
        startup_keyboard = create_startup_inline_kb()
        await callback.message.answer(
            text="<strong>Выберите интересующий вас раздел:</strong>",
            reply_markup=startup_keyboard,
        )

        stikers_keyboard = create_stickers_inline_kb()
        await callback.message.answer(
            text=LEXICON_RU["stickers"], reply_markup=stikers_keyboard
        )
        bonus_keyboard = create_bonus_inline_kb()
        await callback.message.answer(
            text=LEXICON_RU["bonus"], reply_markup=bonus_keyboard
        )


@router.message(Command(commands="bonus"))
async def process_bonus_command(message: Message):
    bonus_keyboard = create_bonus_inline_kb()
    await message.answer(text=LEXICON_RU["bonus"], reply_markup=bonus_keyboard)

    stikers_keyboard = create_stickers_inline_kb()
    await message.answer(text=LEXICON_RU["stickers"], reply_markup=stikers_keyboard)


@router.callback_query(F.data == "bonus")
async def process_bonus_press(callback: CallbackQuery):
    bonus_keyboard = create_bonus_inline_kb()
    if callback.message is not None:
        await callback.message.answer(
            text=LEXICON_RU["bonus"], reply_markup=bonus_keyboard
        )

        stikers_keyboard = create_stickers_inline_kb()
        await callback.message.answer(
            text=LEXICON_RU["stickers"], reply_markup=stikers_keyboard
        )


@router.message(Command(commands="feedback"))
async def process_feedback_command(message: Message):
    faq_dict: Dict[str, Any] = get_faq_sections()
    text = faq_dict["reviews"]["write_review"]["answer"]
    feedback_keyboard = create_feedback_inline_kb()
    await message.answer(text=text, reply_markup=feedback_keyboard)


@router.callback_query(F.data == "feedback")
async def process_feedback_press(callback: CallbackQuery):
    faq_dict: Dict[str, Any] = get_faq_sections()
    text = faq_dict["reviews"]["write_review"]["answer"]
    feedback_keyboard = create_feedback_inline_kb()
    if callback.message is not None:
        await callback.message.answer(text=text, reply_markup=feedback_keyboard)
