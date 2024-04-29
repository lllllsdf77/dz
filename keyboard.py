from aiogram import types

def start_keyboard():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Контакты', callback_data='contact'),
                types.InlineKeyboardButton(text='Пожелания', callback_data='wish')
            ],
            [
                types.InlineKeyboardButton(text='Оставить отзыв', callback_data='survey')
            ],
            [
                types.InlineKeyboardButton(text='Проверить сайт домов', callback_data='check')
            ]
        ]
    )
    return kb
