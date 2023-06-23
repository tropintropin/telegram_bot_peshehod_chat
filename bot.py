import asyncio

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config


async def main() -> None:
    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


# Работающий вариант бота:

# env: Env = Env()
# env.read_env('.env')

# bot: Bot = Bot(token=env('BOT_TOKEN'), parse_mode='HTML')  # NB! Change token for the prod bot!
# dp: Dispatcher = Dispatcher()


# @dp.message(Command(commands=['start']))
# async def process_start_command(message: Message):
#     # TODO: Добавить задержку между сообщениями
#     await message.answer(f'{greeting}')
#     sleep(2)
#     await message.answer(f'{instruction}')
#     sleep(2)
#     await message.answer('<pre><code>Наш бот находится в разработке, скоро здесь появится новый функционал 🤗</code></pre>')



# @dp.message()       # for all other messages
# async def send_echo(message: Message):
#     await message.reply(text='''
# Для справки введите или нажмите /help
# Нажмите /start, чтобы вернуться в начало''')


# if __name__ == '__main__':
#     dp.run_polling(bot)

