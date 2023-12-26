"""Inline keyboards for the bot.
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config_data.config import (FAQCallbackFactory, ItemsFAQCallbackFactory,
                                ToursCallbackFactory,
                                TourSpecItemCallbackFactory)
from lexicon.lexicon import LEXICON_RU, LEXICON_COMMANDS
from services.services import cut_tour_specs_for_keyboard


def create_startup_inline_kb() -> InlineKeyboardMarkup:
    """DOCSTRING""" #TODO
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='❓ Частые вопросы и ответы', callback_data='faq'),
        InlineKeyboardButton(text='📃 Список всех туров', callback_data='tours'),
        InlineKeyboardButton(text='🎲 Подобрать себе тур', callback_data='choose_tour'),
        InlineKeyboardButton(text='🆘 Справка', callback_data='help'),
        InlineKeyboardButton(text='☎ Контакты', callback_data='contacts')
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()


def create_cancel_button() -> InlineKeyboardButton:
    cancel_button: InlineKeyboardButton = InlineKeyboardButton(
        text=LEXICON_COMMANDS['/cancel'],
        callback_data='cancel')
    return cancel_button


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
        InlineKeyboardButton(text='👨‍👩‍👦 Групповые', callback_data='group_tours'),
        InlineKeyboardButton(text='💃 Индивидуальные', callback_data='private_tours')
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
        text='⬇ К списку всех туров',
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
        text='⬇ К списку всех туров',
        callback_data='tours'
    )

    kb_builder.row(*buttons, width=width)
    kb_builder.row(button_tours)

    return kb_builder.as_markup()


def create_faq_section_list_inline_kb(width: int, user_dict: dict) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for callback, section in user_dict.items():
        buttons.append(InlineKeyboardButton(
            text=section['section_name'],
            callback_data=FAQCallbackFactory(section=callback).pack()
        ))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()


def create_faq_section_item_inline_kb(width: int, user_dict: dict, section: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for callback, item in user_dict.items():
        buttons.append(InlineKeyboardButton(
            text=item['question'],
            callback_data=ItemsFAQCallbackFactory(section=section, item=callback).pack()
        ))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()


def create_tour_selection_inline_kb(width: int, user_dict: dict) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder() = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for callback, question in user_dict.items():
        if callback != 'question':
            buttons.append(InlineKeyboardButton(
                text=question,
                callback_data=callback
            ))

    kb_builder.row(*buttons, width=width)
    kb_builder.row(create_cancel_button(), width=1)

    return kb_builder.as_markup()
