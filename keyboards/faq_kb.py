from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

import json


with open('lexicon/faq.json', 'r', encoding='utf-8') as faq:
    sections: dict = json.load(faq)['sections']


with open('lexicon/tours_list.json', 'r', encoding='utf-8') as tours_list:
    tours: dict = json.load(tours_list)['tours']


kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()


def create_faq_keyboard(*buttons: str):
    kb_builder.row(*tours.keys(), width=1)
    return kb_builder
    # TODO: Сделать хендлер для генерации этой клавиатуры


# Создаем объекты кнопок клавиатуры
# Создаем объект клавиатуры
# Добавляем массивы нужной конфигурации с кнопками в основной массив клавиатуры

# print('\n\n'.join(tours.keys()))