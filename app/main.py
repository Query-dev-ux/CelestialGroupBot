import asyncio
import ssl
import logging
from app.bot import bot, dp
from app.handlers import register_handlers
from app.server import start_server

logging.basicConfig(level=logging.INFO)


async def main():
    register_handlers(dp)
    runner = await start_server()
    logging.info("Ping server started on http://0.0.0.0:8080/ping")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await runner.cleanup()


if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    if hasattr(asyncio, "WindowsProactorEventLoopPolicy"):
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
