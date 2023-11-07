'''Handlers for the Tour Selection Form Section.
'''

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.redis import Redis, RedisStorage
from aiogram.types import CallbackQuery, Message

from services.fsm import FSMTourSelection
