'''Here are the handlers for the FAQ Section.
'''
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.array_keyboards import create_tours_list_inline_kb
from services.services import get_faq_sections, get_tours_list


router: Router = Router()


@router.message(Command(commands='tours'))
async def process_tours_command(message: Message):
    keyboard = create_tours_list_inline_kb(1, get_tours_list())
    await message.answer(text='Список всех туров:', reply_markup=keyboard)


@router.message(Command(commands='faq'))
async def process_faq_command(message: Message):
    sections = get_faq_sections()
    # TODO: Create keyboard from list
    await message.answer(text='\n\n'.join(sections.keys()))


# В расписание всех групповых туров надо добавить фразу
# "в графике возможны изменения, актуальное расписание на сайте",
# ну или что-то такое
