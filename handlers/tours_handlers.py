"""Handlers for the "Tours" section.
"""

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from config_data.config import ToursCallbackFactory, TourSpecItemCallbackFactory
from keyboards.inline_keyboards import (
    create_tour_specs_inline_kb,
    create_tours_inline_kb,
    create_tours_list_inline_kb,
)
from lexicon.lexicon import LEXICON_RU
from services.services import (
    get_group_tours_list,
    get_private_tours_list,
    get_tour_specs,
    get_tours_list,
)

router: Router = Router()


@router.callback_query(TourSpecItemCallbackFactory.filter())
async def process_tour_spec_item_press(
    callback: CallbackQuery, callback_data: TourSpecItemCallbackFactory
):
    """
    Handle the callback query when a tour specification item's button is pressed.

    This function processes the callback query when a button associated with a specific tour specification item is pressed.
    It retrieves the tour specifications and sends the corresponding information as a response.
    Additionally, it provides buttons for other tour specifications related to the same tour.

    :param callback: The callback query object representing the user's interaction with the button.
    :type callback: aiogram.types.CallbackQuery
    :param callback_data: The callback data containing the tour and the specific item.
    :type callback_data: TourSpecItemCallbackFactory
    """
    spec = get_tours_list()[callback_data.tours]
    tour_specs = get_tour_specs(callback_data.tours)
    tour_specs_keyboard = create_tour_specs_inline_kb(
        2, tour_specs, callback_data.tours
    )

    if callback.message:
        await callback.message.edit_reply_markup()

        await callback.message.answer(
            text=rf"""<strong>{callback_data.item}</strong>
{spec[callback_data.item]}

<strong>Другие вопросы:</strong>""",
            reply_markup=tour_specs_keyboard,
            parse_mode="HTML",
        )


@router.callback_query(ToursCallbackFactory.filter())
async def process_tour_specs_press(
    callback: CallbackQuery, callback_data: ToursCallbackFactory
):
    """
    Handle the callback query when a tour button is pressed.

    This function processes the callback query when a tour button is pressed.
    It retrieves the tour specifications and sends the corresponding information as a response.

    :param callback: The callback query object.
    :type callback: aiogram.types.CallbackQuery
    :param callback_data: The callback data containing the tour.
    :type callback_data: ToursCallbackFactory
    """

    if callback.message:
        await callback.message.edit_reply_markup()

        tour_specs = get_tour_specs(callback_data.tours)
        tour_specs_keyboard = create_tour_specs_inline_kb(
            2, tour_specs, callback_data.tours
        )
        await callback.message.answer(
            text=rf"""<strong>{tour_specs['Название']}</strong>
{tour_specs['О чём экскурсия?']}

<strong>Дополнительные данные по туру:</strong>""",
            reply_markup=tour_specs_keyboard,
        )


@router.callback_query(F.data == "tours")
async def process_tours_press(callback: CallbackQuery):
    """
    Handle the callback query when the "Tours" button is pressed.

    This function processes the callback query when the "Tours" button is pressed.
    It sends the available tours using an inline keyboard.

    :param callback: The callback query object.
    :type callback: aiogram.types.CallbackQuery
    """

    if callback.message:
        await callback.message.edit_reply_markup()

        tours_keyboard = create_tours_inline_kb()
        await callback.message.answer(
            text=rf"""<strong>Список всех туров</strong>
{LEXICON_RU['tours']}""",
            reply_markup=tours_keyboard,
        )


@router.message(Command(commands="tours"))
async def process_tours_command(message: Message):
    """
    Handle the command "/tours".

    This function processes the command "/tours" and sends
    the available tours using an inline keyboard.

    :param message: The received message object.
    :type message: aiogram.types.Message
    """
    tours_keyboard = create_tours_inline_kb()
    await message.answer(
        text=rf"""<strong>Список всех туров</strong>
{LEXICON_RU['tours']}""",
        reply_markup=tours_keyboard,
    )


@router.callback_query(F.data == "group_tours")
async def process_group_tours_press(callback: CallbackQuery):
    """
    Handle the callback query when the "Group Tours" button is pressed.

    This function processes the callback query when the "Group Tours" button is pressed.
    It sends the list of group tours using an inline keyboard.

    :param callback: The callback query object.
    :type callback: aiogram.types.CallbackQuery
    """

    if callback.message:
        await callback.message.edit_reply_markup()

        group_tours_keyboard = create_tours_list_inline_kb(1, get_group_tours_list())
        await callback.message.answer(
            text=rf"""<strong>ГРУППОВЫЕ ТУРЫ</strong>
{LEXICON_RU['group_tours']}""",
            reply_markup=group_tours_keyboard,
        )


@router.callback_query(F.data == "private_tours")
async def process_private_tours_press(callback: CallbackQuery):
    """
    Handle the callback query when the "Private Tours" button is pressed.

    This function processes the callback query when the "Private Tours" button is pressed.
    It sends the list of private tours using an inline keyboard.

    :param callback: The callback query object.
    :type callback: aiogram.types.CallbackQuery
    """

    if callback.message:
        await callback.message.edit_reply_markup()

        private_tours_keyboard = create_tours_list_inline_kb(
            1, get_private_tours_list()
        )
        await callback.message.answer(
            text=rf"""<strong>ЧАСТНЫЕ ТУРЫ</strong>
{LEXICON_RU['private_tours']}""",
            reply_markup=private_tours_keyboard,
        )
