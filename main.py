import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers import atack_router, location_router, start_router
from settings import setting


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=setting.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(atack_router, location_router, start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
