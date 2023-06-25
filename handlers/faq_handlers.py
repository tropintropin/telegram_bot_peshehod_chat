'''Here are the handlers for the FAQ Section.
'''
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.list_keyboard import create_inline_kb

import json


router: Router = Router()


with open('lexicon/faq.json', 'r', encoding='utf-8') as faq:
    sections: dict = json.load(faq)['sections']


with open('lexicon/tours_list.json', 'r', encoding='utf-8') as tours_list:
    tours: dict = json.load(tours_list)['tours']


@router.message(Command(commands='tours'))
async def process_tours_command(message: Message):
    keyboard = create_inline_kb(1, *tours.keys())
    await message.answer(text='Список всех туров:', reply_markup=keyboard)
    # TODO: Create keyboard from list


@router.message(Command(commands='faq'))
async def process_faq_command(message: Message):
    # TODO: Create keyboard from list
    await message.answer(text='\n\n'.join(sections.keys()))


# В расписание всех групповых туров надо добавить фразу
# "в графике возможны изменения, актуальное расписание на сайте",
# ну или что-то такое
