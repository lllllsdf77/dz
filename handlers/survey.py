from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import database


survey_router = Router()

class BookSurvey(StatesGroup):
    name = State()
    age = State()
    star = State()
    capt = State()


@survey_router.message(Command("stop"))
@survey_router.message(F.text.lower() == "стоп")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за прохождение опроса!")


@survey_router.callback_query(F.data == 'survey')
async def get_survey(cb: types.CallbackQuery, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    await cb.answer()
    await state.set_state(BookSurvey.name)
    await cb.message.answer('Как вас зовут?', reply_markup=kb)

@survey_router.message(BookSurvey.name)
async def name(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.age)
    await state.update_data(name=message.text)
    await message.answer(f'Сколько вам лет, {message.text}?')

@survey_router.message(BookSurvey.age)
async def age(message: types.Message, state: FSMContext):

    agetest = message.text
    if int(agetest) < 10 or int(agetest) > 100:
        await message.answer('Вы слишком малы или мертвы чтобы оставить отзыв.')
        return

    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='⭐'),
                types.KeyboardButton(text='⭐⭐'),
                types.KeyboardButton(text='⭐⭐⭐')
            ],
            [
                types.KeyboardButton(text='⭐⭐⭐⭐'),
                types.KeyboardButton(text='⭐⭐⭐⭐⭐')
            ]],
        resize_keyboard=True
    )
    await state.update_data(age=agetest)
    await state.set_state(BookSurvey.star)
    await message.answer('Поставьте нам оценку:', reply_markup=kb)

@survey_router.message(BookSurvey.star)
async def star(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    stars = len(message.text)
    await state.set_state(BookSurvey.capt)
    await state.update_data(star=stars)
    await message.answer('Напишите что вам понравилось/не понравилось', reply_markup=kb)

@survey_router.message(BookSurvey.capt)
async def capt(message: types.Message, state: FSMContext):
    await state.update_data(capt=message.text)
    data = await state.get_data()
    print('-', data)
    await database.execute('INSERT INTO survey ('
                           'name, age, rate, capt) VALUES ('
                           '?, ?, ?, ?)',
                           (data["name"], data["age"], data['star'], data['capt']))
    await message.answer('Мы отправили ваш отзыв!'
                         f'\nИмя - {data["name"]}'
                         f'\nВозраст - {data["age"]}'
                         f'\nОценка - {data["star"]}'
                         f'\nОтзыв - {data["capt"]}.'
                         )
    await state.clear()
