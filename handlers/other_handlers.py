from aiogram.types import Message


@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except:
        await message.reply(text='Упс, я вас не понимаю... Попробуйте задать верную команду. Для справки нажмите /help')

