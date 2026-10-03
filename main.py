import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher
from handlers import start, echo

# Loglarni sozlash
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

async def main():
    # BOT_TOKEN ni muhit o'zgaruvchilaridan (env vars) oqish
    bot_token = os.getenv("BOT_TOKEN")
    
    if not bot_token:
        logging.error("BOT_TOKEN ortam o'zgaruvchisi topilmadi!")
        sys.exit(1)

    bot = Bot(token=bot_token)
    dp = Dispatcher()

    # Handlerni ro'yxatdan o'tkazish
    dp.include_router(start.router)
    dp.include_router(echo.router)  # Echo har doim oxirida bo'lishi kerak

    logging.info("Bot ishga tushmoqda...")
    
    # Long polling rejimida ishga tushirish
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())