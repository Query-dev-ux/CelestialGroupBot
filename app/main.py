import asyncio
import ssl
import logging
from app.bot import bot, dp
from app.handlers import register_handlers

logging.basicConfig(level=logging.INFO)


async def main():
    register_handlers(dp)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
