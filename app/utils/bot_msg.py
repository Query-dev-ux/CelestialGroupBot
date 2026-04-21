from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


async def safe_delete(message: Message):
    try:
        await message.delete()
    except Exception:
        pass


async def edit_or_replace(bot: Bot, chat_id: int, state: FSMContext, text: str, reply_markup=None, parse_mode="HTML"):
    """Try to edit the tracked bot message. On failure, delete it and send a new one."""
    data = await state.get_data()
    bot_msg_id = data.get("bot_msg_id")
    if bot_msg_id:
        try:
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=bot_msg_id,
                text=text,
                reply_markup=reply_markup,
                parse_mode=parse_mode,
            )
            return
        except Exception:
            try:
                await bot.delete_message(chat_id, bot_msg_id)
            except Exception:
                pass
    sent = await bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup, parse_mode=parse_mode)
    await state.update_data(bot_msg_id=sent.message_id)
