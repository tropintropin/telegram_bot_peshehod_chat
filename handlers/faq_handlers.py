'''Here are the handlers for the FAQ Section.
'''
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards

import json


router: Router = Router()


with open('lexicon/faq.json', 'r', encoding='utf-8') as faq:
    sections: dict = json.load(faq)['sections']


with open('lexicon/tours_list.json', 'r', encoding='utf-8') as tours_list:
    tours: dict = json.load(tours_list)['tours']


@router.message(Command(commands='tours'))
async def process_tours_command(message: Message):
    # TODO: Create keyboard from list
    # await message.answer(text='\n\n'.join(tours.keys()))


@router.message(Command(commands='faq'))
async def process_faq_command(message: Message):
    # TODO: Create keyboard from list
    # await message.answer(text='\n\n'.join(sections.keys()))

