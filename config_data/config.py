"""Bot configuration data, including its token.
Classes for generating callback data for buttons.
"""

from aiogram.filters.callback_data import CallbackData
from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


# If the path is not specified, the current directory will be used.
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))


# Factory for creating callback data for tour-related buttons.
class ToursCallbackFactory(CallbackData, prefix='t'):
    tours: str


# Callback data will be associated with specific tours or tour elements.
class TourSpecItemCallbackFactory(ToursCallbackFactory, prefix='i'):
    item: str
