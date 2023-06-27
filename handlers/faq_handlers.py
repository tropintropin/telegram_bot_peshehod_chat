'''Here are the handlers for the FAQ Section.
'''
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.array_keyboards import create_tours_inline_kb, create_tours_list_inline_kb, create_tour_specs_inline_kb
from lexicon.lexicon import LEXICON_RU
from services.services import get_faq_sections, get_tour_specs, get_group_tours_list, get_private_tours_list


router: Router = Router()


@router.message(Command(commands='tours'))
async def process_tours_command(message: Message):
    tours_keyboard = create_tours_inline_kb()
    await message.answer(text=LEXICON_RU['tours'], reply_markup=tours_keyboard)


@router.message(Command(commands='group_tours'))
async def process_group_tours_command(message: Message):
    group_tours_keyboard = create_tours_list_inline_kb(1, get_group_tours_list())
    await message.answer(text=LEXICON_RU['group_tours'], reply_markup=group_tours_keyboard)


@router.message(Command(commands='private_tours'))
async def process_private_tours_command(message: Message):
    private_tours_keyboard = create_tours_list_inline_kb(1, get_private_tours_list())
    await message.answer(text=LEXICON_RU['private_tours'], reply_markup=private_tours_keyboard)


@router.message(Command(commands='faq'))
async def process_faq_command(message: Message):
    sections = get_faq_sections()
    # TODO: Create keyboard from list
    await message.answer(text='\n\n'.join(sections.keys()))


# В расписание всех групповых туров надо добавить фразу
# "в графике возможны изменения, актуальное расписание на сайте",
# ну или что-то такое

