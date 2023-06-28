from aiogram.filters.callback_data import CallbackData
from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))


class ToursCallbackFactory(CallbackData, prefix='tours'):
    tours: str


class TourSpecItemCallbackFactory(CallbackData, prefix='item'):
    item: str


