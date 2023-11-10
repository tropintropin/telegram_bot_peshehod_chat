"""Bot configuration data, including its token and storage.
Classes for generating callback data for buttons.
"""

from dataclasses import dataclass

from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.storage.redis import RedisStorage
from environs import Env
from redis.asyncio.client import Redis


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
class Storage:
    """
    Represents the storage configuration for the bot.

    This data class encapsulates the RedisStorage instance used for data storage.

    :param redis_storage: The RedisStorage instance.
    :type redis_storage: RedisStorage
    """

    redis_storage: RedisStorage


@dataclass
class Config:
    """
    Represents the configuration for the bot.

    This data class encapsulates the Telegram Bot configuration and storage configuration.

    :param tg_bot: The Telegram Bot configuration.
    :type tg_bot: TgBot
    :param storage: The storage configuration.
    :type storage: Storage
    """

    tg_bot: TgBot
    storage: Storage


def load_config(path: str | None = None) -> Config:
    """
    Load the configuration data from the specified environment file.

    This function reads the configuration data, including the Telegram Bot token,
    from the specified environment file (or the current directory if not specified).
    It also configures the Redis-based storage for the bot.

    :param path: The path to the environment file (default is None).
    :type path: str or None
    :return: The Config object with the loaded configuration data.
    :rtype: Config
    """
    env = Env()
    env.read_env(path)
    redis: Redis = Redis(host="localhost", db=0)
    return Config(
        tg_bot=TgBot(token=env("BOT_TOKEN")),
        storage=Storage(redis_storage=RedisStorage(redis=redis))
    )


class FAQCallbackFactory(CallbackData, prefix="f"):
    """
    Factory for creating callback data related to frequently asked questions (FAQ).

    This class extends the CallbackData class and adds a prefix 'f' to all generated callback data.

    :param section: #TODO
    :type section: str
    """

    section: str


class ItemsFAQCallbackFactory(FAQCallbackFactory, prefix="fi"):
    """
    Factory for creating callback data related to specific items in frequently asked questions (FAQ).

    This class extends the FAQCallbackFactory class and adds a prefix 'fi' to all generated callback data.

    :param item: #TODO
    :type item: str
    """

    item: str


class ToursCallbackFactory(CallbackData, prefix="t"):
    """
    Factory for creating callback data for tour-related buttons.

    This class extends the CallbackData class and adds a prefix 't' to all generated callback data.

    :param tours: The data related to tours to be included in the callback.
    :type tours: str
    """

    tours: str


class TourSpecItemCallbackFactory(ToursCallbackFactory, prefix="i"):
    """
    Factory for creating callback data for specific tour elements.

    This class extends the ToursCallbackFactory class and adds a prefix 'i' to all generated callback data.

    :param item: The specific tour element to be included in the callback.
    :type item: str
    """

    item: str
