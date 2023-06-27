from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON_RU


# Создаем объекты кнопок клавиатуры
# Создаем объект клавиатуры
# Добавляем массивы нужной конфигурации с кнопками в основной массив клавиатуры

def create_tours_inline_kb() -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(text='Групповые туры', callback_data='group_tours'),
        InlineKeyboardButton(text='Индивидуальные туры', callback_data='private_tours')
    ]
    kb_builder.row(*buttons, width=2)
    return kb_builder.as_markup()


def create_tours_list_inline_kb(width: int, user_dict: dict[str, dict[str, str]]) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for button, name in user_dict.items():
        buttons.append(InlineKeyboardButton(
            text=name['Название'],
            callback_data=button
        ))

    button_tours = InlineKeyboardButton(
        text='К списку всех туров',
        callback_data='tours'
    )

    kb_builder.row(*buttons, width=width)
    kb_builder.row(button_tours)

    return kb_builder.as_markup()


def create_tour_specs_inline_kb(width: int, user_dict: dict[str, str | dict]) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for key in ['is_group_tour', 'Название', 'О чём экскурсия?']:
        user_dict.pop(key, None)

    for name, description in user_dict.items():
        buttons.append(InlineKeyboardButton(
            text=name,
            callback_data='CALLBACK'  # TODO: Change callback to description's value
        ))

    button_tours = InlineKeyboardButton(
        text='К списку всех туров',
        callback_data='tours'
    )

    kb_builder.row(*buttons, width=width)
    kb_builder.row(button_tours)

    return kb_builder.as_markup()
    
