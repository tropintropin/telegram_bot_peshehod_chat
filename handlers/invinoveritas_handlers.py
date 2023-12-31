"""Handlers for the Wine Lections Section
"""

import logging

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from handlers.user_handlers import process_bonus_press
from keyboards.inline_keyboards import create_invinoveritas_inline_kb
from lexicon.lexicon import LEXICON_RU
from services.fsm import FSMInvinoveritas
from services.services import get_invinoveritas_list

router: Router = Router()


@router.message(Command(commands="invinoveritas"))
async def process_invinoveritas_command(message: Message, state: FSMContext):
    """
    Processes the "invinoveritas" command. 
    Retrieves the "invinoveritas" lectures list, creates a keyboard for selecting a lecture, and sends it along with a message to the user.
    Then sets the FSM state to "lection".
    """
    invinoveritas_list = get_invinoveritas_list()
    invinoveritas_keyboard = create_invinoveritas_inline_kb(1, invinoveritas_list)
    text = f"<strong>ВИННЫЕ ХРОНИКИ 🔞</strong>\n\n{LEXICON_RU['invinoveritas']}"
    await message.answer(text=text, reply_markup=invinoveritas_keyboard)
    await state.set_state(FSMInvinoveritas.lection)


@router.callback_query(F.data == "invinoveritas")
async def process_invinoveritas_press(callback: CallbackQuery, state: FSMContext):
    """
    Processes the "invinoveritas" button press. 
    Retrieves the "invinoveritas" lectures list, creates a keyboard for selecting a lecture, and sends it along with a message to the user.
    Then sets the FSM state to "lection".
    """
    if callback.message:
        invinoveritas_list = get_invinoveritas_list()
        invinoveritas_keyboard = create_invinoveritas_inline_kb(1, invinoveritas_list)
        text = f"<strong>ВИННЫЕ ХРОНИКИ 🔞</strong>\n\n{LEXICON_RU['invinoveritas']}"
        await callback.message.answer(text=text, reply_markup=invinoveritas_keyboard)
        await state.set_state(FSMInvinoveritas.lection)


@router.callback_query(StateFilter(FSMInvinoveritas.lection))
async def process_lection_sent(callback: CallbackQuery, state: FSMContext):
    """
    Processes the sent lecture. 
    Extracts lecture information from the "invinoveritas" lectures list and sends it to the user.
    If lecture information is not found or if there is no message or data, logs an error.
    """
    if callback.message is not None and callback.data is not None:
        lecture_info = get_invinoveritas_list().get(callback.data)
        if lecture_info is not None:
            text = f"""<strong>{lecture_info['Название']}</strong>

{lecture_info["Описание"]}

<strong>Лектор:</strong> {lecture_info["Лектор"]}

<strong>Дата:</strong> {lecture_info["Дата"]}

<strong>Место:</strong> {lecture_info["Место"]}

<strong>Цены:</strong>
{lecture_info["Цены"]}

<i>{lecture_info["Забронировать"]}</i>
"""
            await callback.message.answer(text=text, parse_mode="HTML")
            await process_bonus_press(callback)
        else:
            logging.error(f"Lecture info not found for data: {callback.data}")
            await callback.message.answer(text="Извините, лекция не найдена.")
    else:
        logging.error(
            f"Missing message or data: message={callback.message}, data={callback.data}"
        )
