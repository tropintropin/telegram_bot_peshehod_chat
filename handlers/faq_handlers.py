'''Here are the handlers for the FAQ Section.
'''
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.list_keyboard import create_tours_inline_kb
from services.services import get_faq_sections, get_tours_list


router: Router = Router()


@router.message(Command(commands='tours'))
async def process_tours_command(message: Message):
    tours = get_tours_list()
    keyboard = create_tours_inline_kb(1, tours, *tours.keys())
    await message.answer(text='Список всех туров:', reply_markup=keyboard)
    # TODO: Create keyboard from list


@router.message(Command(commands='faq'))
async def process_faq_command(message: Message):
    sections = get_faq_sections()
    # TODO: Create keyboard from list
    await message.answer(text='\n\n'.join(sections.keys()))


# В расписание всех групповых туров надо добавить фразу
# "в графике возможны изменения, актуальное расписание на сайте",
# ну или что-то такое
