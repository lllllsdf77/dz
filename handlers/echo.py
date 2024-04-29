from aiogram import Router, types
echo_router = Router()

@echo_router.message()
async def echo(message: types.Message):
    kb = types.ReplyKeyboardRemove
    await message.answer('Я вас не понимаю, если что есть кнопки и команды).')