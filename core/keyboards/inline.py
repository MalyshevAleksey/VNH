from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Частые вопросы❔', callback_data='faq')
    keyboard_builder.button(text='Адреса корпусов🏠', callback_data='addresses')
    keyboard_builder.button(text='Для абитуриентов‍🎓', callback_data='applicants')
    keyboard_builder.button(text='Сайт СамГТУ🎰', url='https://samgtu.ru/')
    keyboard_builder.button(text='Задать вопрос💁‍', callback_data='chat_mode')

    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def back_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Вернуться в меню🏠', callback_data='global')

    return keyboard_builder.as_markup()

def cancel_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Прекратить', callback_data='chat_mode_off')

    return keyboard_builder.as_markup()