"""Handlers for the Wine Lections Section
"""

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

router: Router = Router()


@router.callback_query(F.data == "invinoveritas")
async def process_invinoveritas_press(callback: CallbackQuery)
    pass


@router.message(Command(commands="invinoveritas"))
async def process_invinoveritas_command(message: Message)
    pass