"""Inline keyboards for the bot.
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config_data.config import ToursCallbackFactory, TourSpecItemCallbackFactory
from lexicon.lexicon import LEXICON_RU
from services.services import cut_tour_specs_for_keyboard


def create_tours_inline_kb() -> InlineKeyboardMarkup:
    """
    Create an inline keyboard with two buttons: 'Group Tours' and 'Private Tours'.

    This function creates an inline keyboard with two buttons: 'Group Tours' and 'Private Tours'.
    It returns the created keyboard with the buttons.

    :return: The InlineKeyboardMarkup object with the 'Group Tours' and 'Private Tours' buttons.
    :rtype: InlineKeyboardMarkup
    """
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Групповые туры', callback_data='group_tours'),
        InlineKeyboardButton(text='Индивидуальные туры', callback_data='private_tours')
    ]
    kb_builder.row(*buttons, width=2)
    return kb_builder.as_markup()


def create_tours_list_inline_kb(width: int, user_dict: dict[str, dict[str, str]]) -> InlineKeyboardMarkup:
    """
    Create an inline keyboard with buttons for the list of tours.

    This function creates an inline keyboard with buttons for each tour in the given 'user_dict'.
    It returns the created keyboard with the tour buttons and a button to return to the list of tours.

    :param width: The width of the keyboard (number of buttons in a row).
    :type width: int
    :param user_dict: The dictionary containing information about tours.
    :type user_dict: dict[str, dict[str, str]]
    :return: The InlineKeyboardMarkup object with tour buttons and a button to return to the list of tours.
    :rtype: InlineKeyboardMarkup
    """
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


def create_tour_specs_inline_kb(width: int, user_dict: dict[str, str | dict], tour) -> InlineKeyboardMarkup:
    """
    Create an inline keyboard with buttons for the list of tour specifications.

    This function creates an inline keyboard with buttons for each tour specification in the given 'user_dict'.
    It returns the created keyboard with the tour specification buttons and a button to return to the list of tours.

    :param width: The width of the keyboard (number of buttons in a row).
    :type width: int
    :param user_dict: The dictionary containing information about tour specifications.
    :type user_dict: dict[str, str | dict]
    :param tour: The name of the tour associated with the specifications.
    :type tour: str
    :return: The InlineKeyboardMarkup object with tour specification buttons and a button to return to the list of tours.
    :rtype: InlineKeyboardMarkup
    """
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    specs: dict = cut_tour_specs_for_keyboard(user_dict)

    for name in specs.keys():
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


def create_faq_section_list_inline_kb(width: int, user_dict: dict) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for section, content in user_dict.items():
        buttons.append(InlineKeyboardButton(
            text=section,
            callback_data=content['callback']
        ))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()
