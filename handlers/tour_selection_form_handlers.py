"""Handlers for the Tour Selection Form Section.
"""

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.redis import Redis, RedisStorage
from aiogram.types import CallbackQuery, Message

from services.fsm import FSMTourSelection
from services.services import get_tour_selection
from keyboards.inline_keyboards import create_tour_selection_inline_kb

router: Router = Router()


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
