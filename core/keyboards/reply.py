from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Главное меню')

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите действие в меню⬆:')
