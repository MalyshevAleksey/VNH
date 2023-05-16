import asyncio
import logging

import websocket
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from core.settings import settings
from core.handlers.basic import get_start, any_text, global_menu
from core.handlers.faq import faq, addresses, applicants
from core.handlers.chat import chat, test
from core.utils.chat_state import ChatMode


# системные сообщения
async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'Бот остановлен')


# регистрация хэндлеров
async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(test, ChatMode.GET_MESSAGE)
    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(any_text, F.text)
    dp.callback_query.register(faq, F.data == 'faq')
    dp.callback_query.register(addresses, F.data == 'addresses')
    dp.callback_query.register(applicants, F.data == 'applicants')
    dp.callback_query.register(global_menu, F.data == 'global')
    dp.callback_query.register(chat, F.data == 'chat_mode')
    dp.callback_query.register(chat, F.data == 'chat_mode_off')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())


