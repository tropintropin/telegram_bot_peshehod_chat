"""Handlers for the Tour Selection Form Section.
"""

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from redis.asyncio.client import Redis

from keyboards.inline_keyboards import (
    create_bonus_inline_kb,
    create_stickers_inline_kb,
    create_startup_inline_kb,
    create_tour_selection_inline_kb,
    create_tours_list_inline_kb,
)
from handlers.user_handlers import process_bonus_press
from lexicon.lexicon import LEXICON_RU
from services.fsm import FSMTourSelection
from services.services import get_custom_list_of_tours, get_tour_selection
from services.sqlite_database_handler import get_tours_list

router: Router = Router()


@router.callback_query(F.data == "cancel", ~StateFilter(default_state))
async def process_cancel_press(callback: CallbackQuery, state: FSMContext):
    if callback.message:
        await callback.message.edit_reply_markup()

        await callback.message.answer(text=LEXICON_RU["/cancel"])
        await callback.message.answer(text=LEXICON_RU["/help"])
        
        startup_keyboard = create_startup_inline_kb()
        await callback.message.answer(
            text="<strong>Выберите интересующий вас раздел:</strong>",
            reply_markup=startup_keyboard,
        )

        await process_bonus_press(callback)

        await state.clear()


@router.message(Command(commands="choose_tour"))
async def process_choose_tour_command(message: Message, state: FSMContext):
    """
    Handle the command "/choose_tour".
    """
    questions = get_tour_selection()
    is_group_keyboard = create_tour_selection_inline_kb(
        width=2, user_dict=questions["is_group"]
    )
    await message.answer(
        text=questions["is_group"]["question"], reply_markup=is_group_keyboard
    )
    await state.set_state(FSMTourSelection.is_group)


@router.callback_query(F.data == "choose_tour")
async def process_choose_tour_press(callback: CallbackQuery, state: FSMContext):
    if callback.message:
        await callback.message.edit_reply_markup()

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
        await callback.message.edit_reply_markup()

        await state.update_data(is_group=callback.data)
        questions = get_tour_selection()
        is_group_keyboard = create_tour_selection_inline_kb(
            width=2, user_dict=questions["have_children"]
        )
        await callback.message.answer(
            text=questions["have_children"]["question"], reply_markup=is_group_keyboard
        )
        await state.set_state(FSMTourSelection.have_children)


@router.callback_query(StateFilter(FSMTourSelection.have_children), F.data == "kids")
async def process_have_children_sent(callback: CallbackQuery, state: FSMContext):
    if callback.message:
        await callback.message.edit_reply_markup()

        await state.update_data(have_children=callback.data)

        questions = get_tour_selection()
        is_group_keyboard = create_tour_selection_inline_kb(
            width=2, user_dict=questions["kids"]
        )
        await callback.message.answer(
            text=questions["kids"]["question"], reply_markup=is_group_keyboard
        )
        await state.set_state(FSMTourSelection.kids)


@router.callback_query(StateFilter(FSMTourSelection.have_children), F.data == "adults")
async def process_not_have_children_sent(callback: CallbackQuery, state: FSMContext):
    if callback.message:
        await callback.message.edit_reply_markup()

        await state.update_data(have_children=callback.data)
        await state.update_data(kids=None)

        questions = get_tour_selection()
        is_group_keyboard = create_tour_selection_inline_kb(
            width=2, user_dict=questions["visit"]
        )
        await callback.message.answer(
            text=questions["visit"]["question"], reply_markup=is_group_keyboard
        )
        await state.set_state(FSMTourSelection.visit)


@router.callback_query(StateFilter(FSMTourSelection.kids))
async def process_kids_sent(callback: CallbackQuery, state: FSMContext):
    if callback.message:
        await callback.message.edit_reply_markup()

        await state.update_data(kids=callback.data)

        questions = get_tour_selection()
        is_group_keyboard = create_tour_selection_inline_kb(
            width=2, user_dict=questions["visit"]
        )
        await callback.message.answer(
            text=questions["visit"]["question"], reply_markup=is_group_keyboard
        )
        await state.set_state(FSMTourSelection.visit)


@router.callback_query(StateFilter(FSMTourSelection.visit))
async def process_visit_sent(callback: CallbackQuery, state: FSMContext):
    if callback.message:
        await callback.message.edit_reply_markup()

        await state.update_data(visit=callback.data)

        user_answers = {}
        user_answers[callback.from_user.id] = await state.get_data()

        await state.clear()

        answers = get_tours_list(user_answers[callback.from_user.id])
        tours_list_for_visitor = get_custom_list_of_tours(answers)

        tours_list_inline_kb = create_tours_list_inline_kb(1, tours_list_for_visitor)

        retake_servey = InlineKeyboardButton(
            text="🔄 Пройти тест заново", callback_data="tour_select"
        )
        kb_builder = InlineKeyboardBuilder()
        kb_builder.attach(InlineKeyboardBuilder.from_markup(tours_list_inline_kb))
        kb_builder.row(retake_servey)

        new_tours_list_inline_kb = kb_builder.as_markup()

        await callback.message.answer(
            text="Предлагаем вам обратить внимание на туры, которые мы подобрали специально для вас.\nВпрочем, вы всегда можете ознакомиться со всеми нашими турами по кнопке ниже.",
            reply_markup=new_tours_list_inline_kb,
        )

        await process_bonus_press(callback)
