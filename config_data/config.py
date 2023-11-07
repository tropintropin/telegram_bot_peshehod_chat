"""Bot configuration data, including its token.
Classes for generating callback data for buttons.
"""

from dataclasses import dataclass
from environs import Env

from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.storage.redis import Redis, RedisStorage


@dataclass
class TgBot:
    """
    Represents the Telegram Bot configuration data.

    This data class holds the token required for the Telegram Bot.

    :param token: The Telegram Bot token.
    :type token: str
    """
    token: str


@dataclass
class Config:
    """
    Represents the configuration for the bot.

    This data class encapsulates the Telegram Bot configuration.

    :param tg_bot: The Telegram Bot configuration.
    :type tg_bot: TgBot
    """
    tg_bot: TgBot


@dataclass
class Storage:
    storage: RedisStorage


def load_config(path: str | None = None) -> Config:
    """
    Load the configuration data from the specified environment file.

    This function reads the configuration data, including the Telegram Bot token,
    from the specified environment file (or the current directory if not specified).

    :param path: The path to the environment file (default is None).
    :type path: str or None
    :return: The Config object with the loaded configuration data.
    :rtype: Config
    """
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))


def load_storage() -> Storage:
    redis: Redis = Redis(host='localhost')
    return Storage(storage=Storage.storage(redis=redis))


class FAQCallbackFactory(CallbackData, prefix='f'):
    section: str


class ItemsFAQCallbackFactory(FAQCallbackFactory, prefix='fi'):
    item: str


class ToursCallbackFactory(CallbackData, prefix='t'):
    """
    Factory for creating callback data for tour-related buttons.

    This class extends the CallbackData class and adds a prefix 't' to all generated callback data.

    :param tours: The data related to tours to be included in the callback.
    :type tours: str
    """
    tours: str


class TourSpecItemCallbackFactory(ToursCallbackFactory, prefix='i'):
    """
    Factory for creating callback data for specific tour elements.

    This class extends the ToursCallbackFactory class and adds a prefix 'i' to all generated callback data.

    :param item: The specific tour element to be included in the callback.
    :type item: str
    """
    item: str
