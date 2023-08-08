'''Handlers for the "FAQ" section.
'''

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from config_data.config import FAQCallbackFactory, ItemsFAQCallbackFactory
from keyboards.inline_keyboards import (create_faq_section_item_inline_kb,
                                        create_faq_section_list_inline_kb)
from services.services import cut_faq_section_items, get_faq_sections
from handlers.tours_handlers import process_tours_press


router: Router = Router()


@router.callback_query(ItemsFAQCallbackFactory.filter())
async def process_faq_specs_item_press(callback: CallbackQuery,
                                        callback_data: ItemsFAQCallbackFactory):
    if callback_data.item == 'tours':  # Move to Tours Section if true
        await process_tours_press(callback)
    else:
        if callback.message:
            await callback.message.delete()

            items_list = get_faq_sections()[callback_data.section]
            list_name = items_list['section_name']
            items_list = cut_faq_section_items(items_list)
            items_list_keyboard = create_faq_section_item_inline_kb(1, items_list, callback_data.section)
            await callback.message.answer(
                text=fr"<strong>{list_name}</strong>",
                reply_markup=items_list_keyboard
                )

            item_specs = items_list[callback_data.item]
            await callback.message.answer(text=fr"<strong>{item_specs['question']}</strong>")
            await callback.message.answer(text=item_specs['answer'])

        


@router.callback_query(FAQCallbackFactory.filter())
async def process_faq_specs_press(callback: CallbackQuery,
                                    callback_data: FAQCallbackFactory):
    if callback.message:
        sections = get_faq_sections()
        faq_section_keyboard = create_faq_section_list_inline_kb(
            width=1,
            user_dict=sections
            )
    
        section = sections[callback_data.section]
        list_name = section['section_name']
        items_list = cut_faq_section_items(section)
        
        items_list_keyboard = create_faq_section_item_inline_kb(
            width=1,
            user_dict=items_list,
            section=callback_data.section
            )
        
        await callback.message.delete()

        await callback.message.answer(
            text=r'<strong>ЧАВо (список частых вопросов и ответов):</strong>',
            reply_markup=faq_section_keyboard
            )

        await callback.message.answer(
            text=fr'<strong>{list_name}</strong>',
            reply_markup=items_list_keyboard
            )


@router.callback_query(F.data == 'faq')
async def process_faq_press(callback: CallbackQuery):
    """
    Handle the callback query when the "FAQ" button is pressed.

    This function processes the callback query when the "FAQ" button is pressed.
    It sends the sections from the FAQ using an inline keyboard.

    :param callback: The callback query object.
    :type callback: aiogram.types.CallbackQuery
    """

    if callback.message:
        sections = get_faq_sections()
        faq_section_keyboard = create_faq_section_list_inline_kb(
            width=1,
            user_dict=sections
            )

        await callback.message.answer(
            text=r'<strong>ЧАВо (список частых вопросов и ответов):</strong>',
            reply_markup=faq_section_keyboard
            )


@router.message(Command(commands='faq'))
async def process_faq_command(message: Message):
    """
    Handle the command "/faq".

    This function processes the command "/faq" and sends the sections
    from the FAQ using an inline keyboard.

    :param message: The received message object.
    :type message: aiogram.types.Message
    """
    sections = get_faq_sections()
    faq_section_keyboard = create_faq_section_list_inline_kb(
        width=1,
        user_dict=sections
        )

    await message.answer(
        text=fr'<strong>ЧАВо (список частых вопросов и ответов):</strong>',
        reply_markup=faq_section_keyboard
        )
