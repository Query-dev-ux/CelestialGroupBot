from aiogram.types import Message


async def safe_delete(message: Message):
    try:
        await message.delete()
    except Exception:
        pass
