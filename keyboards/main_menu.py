"""Settings for the main menu of the bot.
Commands set using this function will be displayed in the main menu of the bot
"""

from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon import LEXICON_COMMANDS


async def set_main_menu(bot: Bot):
    """
    Sets the commands that will be displayed in the main menu of the bot.

    :param bot: An instance of the Bot class representing the bot to apply the menu.
    :type bot: aiogram.Bot
    """
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
            ) for command, description in LEXICON_COMMANDS.items()
    ]
    await bot.set_my_commands(main_menu_commands)

