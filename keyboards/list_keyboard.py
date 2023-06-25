from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Создаем объекты кнопок клавиатуры
# Создаем объект клавиатуры
# Добавляем массивы нужной конфигурации с кнопками в основной массив клавиатуры


def create_tours_inline_kb(width: int,
                    user_dict,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=str(user_dict[button]['Название']),
                callback_data=button  # TODO: Write short callback data in jsons
            ))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button
            ))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()

