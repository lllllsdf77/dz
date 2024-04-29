from aiogram import F, Router, types
from crawler.house_kg import DomCrawler


check_router = Router()


@check_router.callback_query(F.data == 'check')
async def get_checked(cb: types.CallbackQuery):
    await cb.answer()
    check = DomCrawler()
    test = await check.get_houses()
    for link in test:
        await cb.message.answer(link)
