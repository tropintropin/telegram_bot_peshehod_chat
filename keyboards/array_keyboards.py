from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Создаем объекты кнопок клавиатуры
# Создаем объект клавиатуры
# Добавляем массивы нужной конфигурации с кнопками в основной массив клавиатуры


def create_tours_list_inline_kb(width: int, user_dict: dict[str, dict[str, str]]) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for button, name in user_dict.items():
        buttons.append(InlineKeyboardButton(
            text=name['Название'],
            callback_data=button
        ))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()

def create_tour_specs_inline_kb(width: int, user_dict: dict[str, str | dict]) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for name, description in user_dict.items():
        if name not in ('Название', 'О чём экскурсия?'):
            buttons.append(InlineKeyboardButton(
                text=name,
                callback_data='CALLBACK'  # TODO: Change callback to description's value
            ))

        kb_builder.row(*buttons, width=width)

        return kb_builder.as_markup()
    
