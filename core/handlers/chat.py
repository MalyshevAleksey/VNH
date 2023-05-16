from aiogram import Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from core.utils.chat_state import ChatMode
from core.keyboards.inline import cancel_inline_keyboard
import websocket


async def chat(call: CallbackQuery, state: FSMContext, bot: Bot):
    answer = f'<b>Вы в режиме общения с поддержкой</b>\n\nЗадавайте вопросы'
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=answer, reply_markup=cancel_inline_keyboard())
    await state.set_state(ChatMode.GET_MESSAGE)


async def test(message: Message):
    await message.answer(f'Test')
    user_id = message.from_user.id
    # Отправка сообщения серверу
    ws.send(f'tg {user_id} {message.text}')
    print(f"Sent message: {message}")


ws = websocket.WebSocket()
ws.connect('ws://localhost:8765')