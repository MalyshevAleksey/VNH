from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from core.keyboards.inline import get_inline_keyboard


async def global_menu(call: CallbackQuery, bot: Bot):
    answer = f'<b>Выберите действие в меню ниже:</b>'
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=answer, reply_markup=get_inline_keyboard())


async def get_start(message: Message, bot: Bot):
    await message.answer(f'<b>Приветствую, {message.from_user.first_name}!\nЭто чат с поддержкой СамГТУ.</b>',
                         reply_markup=get_inline_keyboard())


async def any_text(message: Message, bot: Bot):
    await message.answer(f'<b>Выберите действие в меню ниже:</b>',
                         reply_markup=get_inline_keyboard())
