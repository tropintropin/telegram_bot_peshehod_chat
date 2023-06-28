'''Here are the handlers for the FAQ Section.
'''
from aiogram import F, Router
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery

from config_data.config import ToursCallbackFactory, TourSpecItemCallbackFactory
from keyboards.array_keyboards import create_tours_inline_kb, create_tours_list_inline_kb, create_tour_specs_inline_kb
from lexicon.lexicon import LEXICON_RU
from services.services import get_tours_list, get_faq_sections, get_tour_specs, get_group_tours_list, get_private_tours_list


router: Router = Router()


# TODO: Do correct handler!
# TODO: Нужно сделать класс для обработки туров и совать его в get_tours_list()
@router.callback_query(TourSpecItemCallbackFactory.filter())
async def process_tour_spec_item_press(callback: CallbackQuery,
                                callback_data: TourSpecItemCallbackFactory):
    spec = get_tours_list()['vr_petra_ochami']
    await callback.message.answer(text=fr'<strong>{callback_data.item}</strong>')
    await callback.message.answer(text=spec[callback_data.item])


@router.callback_query(ToursCallbackFactory.filter())
async def process_tour_specs_press(callback: CallbackQuery,
                                callback_data: ToursCallbackFactory):
    tour_specs = get_tour_specs(callback_data.tours)

    await callback.message.answer(text=fr"<strong>{tour_specs['Название']}</strong>")
    await callback.message.answer(text=tour_specs['О чём экскурсия?'])

    tour_specs_keyboard = create_tour_specs_inline_kb(1, tour_specs)
    await callback.message.answer(
        text=r'<strong>Дополнительные данные по туру:</strong>',
        reply_markup=tour_specs_keyboard
        )


@router.callback_query(Text(text='tours'))
async def process_tours_press(callback: CallbackQuery):
    tours_keyboard = create_tours_inline_kb()
    await callback.message.answer(
        text=LEXICON_RU['tours'],
        reply_markup=tours_keyboard
        )


@router.message(Command(commands='tours'))
async def process_tours_command(message: Message):
    tours_keyboard = create_tours_inline_kb()
    await message.answer(
        text=LEXICON_RU['tours'],
        reply_markup=tours_keyboard
        )


@router.callback_query(Text(text='group_tours'))
async def process_group_tours_press(callback: CallbackQuery):
    group_tours_keyboard = create_tours_list_inline_kb(1, get_group_tours_list())
    await callback.message.answer(
        text=LEXICON_RU['group_tours'],
        reply_markup=group_tours_keyboard
        )


@router.callback_query(Text(text='private_tours'))
async def process_private_tours_press(callback: CallbackQuery):
    private_tours_keyboard = create_tours_list_inline_kb(1, get_private_tours_list())
    await callback.message.answer(
        text=LEXICON_RU['private_tours'],
        reply_markup=private_tours_keyboard
        )


@router.callback_query(Text(text='faq'))
async def process_faq_press(callback: CallbackQuery):
    sections = get_faq_sections()
    # TODO: Create keyboard from list
    await callback.message.answer(
        text='\n\n'.join(sections.keys())
        )

@router.message(Command(commands='faq'))
async def process_faq_command(message: Message):
    sections = get_faq_sections()
    # TODO: Create keyboard from list
    await message.answer(
        text='\n\n'.join(sections.keys())
        )


# В расписание всех групповых туров надо добавить фразу
# "в графике возможны изменения, актуальное расписание на сайте",
# ну или что-то такое

