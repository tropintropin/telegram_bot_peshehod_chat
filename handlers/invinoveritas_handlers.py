"""Handlers for the Wine Lections Section
"""

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import CallbackQuery, Message
from redis.asyncio.client import Redis

from keyboards.inline_keyboards import create_invinoveritas_inline_kb
from lexicon.lexicon import LEXICON_RU
from services.fsm import FSMInvinoveritas
from services.services import get_invinoveritas_list

router: Router = Router()


@router.message(Command(commands="invinoveritas"))
async def process_invinoveritas_command(message: Message, state: FSMContext):
    invinoveritas_list = get_invinoveritas_list()
    invinoveritas_keyboard = create_invinoveritas_inline_kb(
        1,
        invinoveritas_list
        )
    await message.answer(text=r'<strong>ВИННЫЕ ХРОНИКИ 🔞</strong>')
    await message.answer(
        text=LEXICON_RU['invinoveritas'],
        reply_markup=invinoveritas_keyboard
        )
    await state.set_state(FSMInvinoveritas.lection)


@router.callback_query(F.data == "invinoveritas")
async def process_invinoveritas_press(callback: CallbackQuery, state: FSMContext):
    if callback.message:
        invinoveritas_list = get_invinoveritas_list()
        invinoveritas_keyboard = create_invinoveritas_inline_kb(
            1,
            invinoveritas_list
            )
        await callback.message.answer(text=r'<strong>ВИННЫЕ ХРОНИКИ 🔞</strong>')
        await callback.message.answer(
            text=LEXICON_RU['invinoveritas'],
            reply_markup=invinoveritas_keyboard
            )
        await state.set_state(FSMInvinoveritas.lection)


@router.callback_query(StateFilter(FSMInvinoveritas.lection))
async def process_lection_sent(callback: CallbackQuery, state: FSMContext):
    if callback.message:
        lecture_info = get_invinoveritas_list()[callback.data]
        await callback.message.answer(
            text=f"""<strong>{lecture_info['Название']}</strong>

{lecture_info["Описание"]}

<strong>Лектор:</strong> {lecture_info["Лектор"]}

<strong>Дата:</strong> {lecture_info["Дата"]}

<strong>Место:</strong> {lecture_info["Место"]}

<strong>Цены:</strong>
{lecture_info["Цены"]}

<i>{lecture_info["Забронировать"]}</i>
""",
            parse_mode="HTML"
        )
