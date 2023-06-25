from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Создаем объекты кнопок клавиатуры
# Создаем объект клавиатуры
# Добавляем массивы нужной конфигурации с кнопками в основной массив клавиатуры


def create_tours_list_inline_kb(width: int, user_dict: dict[str, dict]) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for button, name in user_dict.items():
        buttons.append(InlineKeyboardButton(
            text=name['Название'],
            callback_data=button
        ))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()

