from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.config import settings


async def forward_to_hr(bot: Bot, message: Message, state: FSMContext, label: str):
    """Пересылает сообщение пользователя в HR-группу и показывает подтверждение."""
    data = await state.get_data()
    bot_msg_id = data.get("bot_msg_id")

    sender = message.from_user.mention_html()
    await bot.send_message(settings.HR_GROUP_ID, f"{label}\nОт: {sender}")
    await bot.forward_message(settings.HR_GROUP_ID, message.chat.id, message.message_id)

    try:
        await message.delete()
    except Exception:
        pass

    confirmation = "✅ Резюме отправлено! Мы свяжемся с тобой."
    if bot_msg_id:
        try:
            await bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=bot_msg_id,
                text=confirmation,
            )
            return
        except Exception:
            pass

    sent = await message.answer(confirmation)
    await state.update_data(bot_msg_id=sent.message_id)
