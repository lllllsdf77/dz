from aiogram import Router, types
from aiogram.filters import Command
help_router = Router()

@help_router.message(Command('help'))
async def give_help(message: types.Message):
    await message.answer(f'Команда /start для начала диалога.'
                         f'\nКоманда /menu для распечатки меню.')
