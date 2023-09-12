"""The entry point for the bot.
"""

import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers import (faq_handlers, other_handlers, tours_handlers,
                        user_handlers)
from keyboards.main_menu import set_main_menu


async def main() -> None:
    file_log = logging.FileHandler("bot.log")
    console_out = logging.StreamHandler()
    logging.basicConfig(handlers=(file_log, console_out), level=logging.INFO)
    logging.info('Starting bot...')

    # Loads the bot configuration from a file
    config: Config = load_config()

    # Bot and dispatcher initialization
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Connecting handlers
    dp.include_router(user_handlers.router)
    dp.include_router(faq_handlers.router)
    dp.include_router(tours_handlers.router)
    dp.include_router(other_handlers.router)

    # Setting up the main menu
    await set_main_menu(bot)

    # Deleting outdated webhooks from the bot
    await bot.delete_webhook(drop_pending_updates=True)
    # Bot startup
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
