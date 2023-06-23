import asyncio

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers import faq_handlers, other_handlers, user_handlers
from keyboards.main_menu import set_main_menu


async def main() -> None:
    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(faq_handlers.router)
    dp.include_router(other_handlers.router)

    await set_main_menu(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

