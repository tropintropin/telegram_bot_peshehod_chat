"""Handlers for the Tour Selection Form Section.
"""

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import CallbackQuery, Message
from redis.asyncio.client import Redis

from keyboards.inline_keyboards import (create_startup_inline_kb,
                                        create_tour_selection_inline_kb)
from lexicon.lexicon import LEXICON_RU
from services.fsm import FSMTourSelection
from services.services import get_tour_selection

router: Router = Router()


@router.callback_query(F.data == 'cancel', ~StateFilter(default_state))
async def process_cancel_press(callback: CallbackQuery, state: FSMContext):
    if callback.message:
        await callback.message.answer(text=LEXICON_RU['/cancel'])
        await callback.message.answer(text=LEXICON_RU['/help'])
        startup_keyboard = create_startup_inline_kb()
        await callback.message.answer(
            text='<strong>Выберите интересующий вас раздел:</strong>',
            reply_markup=startup_keyboard
        )
        await state.clear()



@router.callback_query(F.data == "tour_select")
async def process_tour_select_press(callback: CallbackQuery, state: FSMContext):
    if callback.message:
        questions = get_tour_selection()
        is_group_keyboard = create_tour_selection_inline_kb(
            width=2, user_dict=questions["is_group"]
        )
        await callback.message.answer(
            text=questions["is_group"]["question"], reply_markup=is_group_keyboard
        )
        await state.set_state(FSMTourSelection.is_group)


@router.callback_query(StateFilter(FSMTourSelection.is_group))
async def process_is_group_sent(callback: CallbackQuery, state: FSMContext):
    if callback.message:
        await state.update_data(is_group=callback.data)
        questions = get_tour_selection()
        is_group_keyboard = create_tour_selection_inline_kb(
            width=2, user_dict=questions["have_children"]
        )
        await callback.message.answer(
            text=questions["have_children"]["question"], reply_markup=is_group_keyboard
        )
        await state.set_state(FSMTourSelection.have_children)