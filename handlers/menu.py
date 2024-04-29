from aiogram import Router, F, types
from aiogram.filters import Command
from config import database


menu_router = Router()
@menu_router.message(Command("menu"))
async def get_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[[
            types.KeyboardButton(text='Суши'),
            types.KeyboardButton(text='Пицца'),
            types.KeyboardButton(text='Рамен')
        ],
        [
            types.KeyboardButton(text='Сеты'),
            types.KeyboardButton(text='Добавки'),
            types.KeyboardButton(text='Салаты')
        ]
        ],
        resize_keyboard=True
    )
    await message.answer(f'Выберите тип еды:', reply_markup=kb)


food = ["пицца", "сеты", "добавки", "рамен", "салаты", 'суши']

@menu_router.message(F.text.lower().in_(food))
async def choose(message: types.Message):
    genre = message.text.lower()
    kb = types.ReplyKeyboardRemove()
    data = await database.fetch(
        '''
        SELECT food.* from food
        JOIN genre ON food.genre_id = genre.id
        WHERE genre.name = ?
        ''',
        (genre,),
        fetch_type='all'
    )
    if not data:
        await message.answer('По вашему запросу ничего не найдено', reply_markup=kb)
    await message.answer(f'Все наши блюда - {genre}:')
    for food in data:
        price = food['price']
        capt = food['capt']
        name = food['name']
        photo = types.FSInputFile(food['picture'])
        await message.answer_photo(
            photo=photo,
            caption=f'Название блюда: {name}\nОписание: {capt}'
                    f'\nЦена: {price} сом.', reply_markup=kb
        )
