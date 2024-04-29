from aiogram import Router, F, types
from aiogram.filters import Command
from text.welcome import welcome
from keyboard import start_keyboard
start_router = Router()

@start_router.message(Command('start'))
async def starting(message: types.Message):
    images = types.FSInputFile("image/image.jpg")
    await message.answer_photo(images,
        f'Добро пожаловать {message.from_user.first_name}'
        f' в Masahiro sushi бар!' + welcome, reply_markup=start_keyboard()
    )

@start_router.callback_query(F.data == 'contact')
async def contact(cb: types.CallbackQuery):
    await cb.message.answer('Номер нашей команды - 0700 980-980')

@start_router.callback_query(F.data == 'wish')
async def wish(cb: types.CallbackQuery):
    await cb.message.answer('Пожелания еще в разработке , извините...')
