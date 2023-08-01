"""Inline keyboards for the Telegram bot.
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config_data.config import ToursCallbackFactory, TourSpecItemCallbackFactory
from lexicon.lexicon import LEXICON_RU
from services.services import cut_tour_specs_for_keyboard


# Creates an inline keyboard with two buttons: "Group Tours" and "Individual Tours"
def create_tours_inline_kb() -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Групповые туры', callback_data='group_tours'),
        InlineKeyboardButton(text='Индивидуальные туры', callback_data='private_tours')
    ]
    kb_builder.row(*buttons, width=2)
    return kb_builder.as_markup()


# Creates an inline keyboard with buttons for the list of tours
def create_tours_list_inline_kb(width: int, user_dict: dict[str, dict[str, str]]) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for button, name in user_dict.items():
        buttons.append(InlineKeyboardButton(
            text=name['Название'],
            callback_data=ToursCallbackFactory(tours=button).pack()
        ))

    button_tours = InlineKeyboardButton(
        text='К списку всех туров',
        callback_data='tours'
    )

    kb_builder.row(*buttons, width=width)
    kb_builder.row(button_tours)

    return kb_builder.as_markup()


# Creates an inline keyboard with buttons for the list of tour specifications
def create_tour_specs_inline_kb(width: int, user_dict: dict[str, str | dict], tour) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    specs: dict = cut_tour_specs_for_keyboard(user_dict)

    for name, description in specs.items():
        buttons.append(InlineKeyboardButton(
            text=name,
            callback_data=TourSpecItemCallbackFactory(tours=tour, item=name).pack()
        ))

    button_tours = InlineKeyboardButton(
        text='К списку всех туров',
        callback_data='tours'
    )

    kb_builder.row(*buttons, width=width)
    kb_builder.row(button_tours)

    return kb_builder.as_markup()
    