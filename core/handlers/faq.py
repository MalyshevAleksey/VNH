from aiogram import Bot
from aiogram.types import CallbackQuery
from core.keyboards.inline import back_inline_keyboard


async def faq(call: CallbackQuery, bot: Bot):
    answer = f'<b>Частые вопросы❔</b>\n\nВопрос: ответ\nВопрос: ответ\nВопрос: ответ\n'
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=answer, reply_markup=back_inline_keyboard())


async def addresses(call: CallbackQuery, bot: Bot):
    answer = f'<b>Адреса корпусов🏠</b>\n\nадрес\nадрес\nадрес'
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=answer, reply_markup=back_inline_keyboard())


async def applicants(call: CallbackQuery, bot: Bot):
    answer = f'<b>Для абитуриентов‍🎓</b>\n\nинформация'
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=answer, reply_markup=back_inline_keyboard())
