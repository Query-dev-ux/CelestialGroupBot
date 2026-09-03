from typing import Optional

from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.config import settings
from app.utils.recruitment import submit_telegram_application


async def forward_to_hr(bot: Bot, message: Message, state: FSMContext, label: str, vacancy_ref: Optional[str] = None):
    """Пересылает сообщение пользователя в HR-группу и показывает подтверждение.

    Также (best-effort, никогда не блокирует пересылку в HR) передаёт отклик
    в Recruitment Service — см. app/utils/recruitment.py.
    """
    data = await state.get_data()
    bot_msg_id = data.get("bot_msg_id")

    sender = message.from_user.mention_html()
    await bot.send_message(settings.HR_GROUP_ID, f"{label}\nОт: {sender}")
    await bot.forward_message(settings.HR_GROUP_ID, message.chat.id, message.message_id)

    await submit_telegram_application(
        telegram_user_id=message.from_user.id,
        vacancy_ref=vacancy_ref,
        candidate_text=message.text,
        resume_file_ref=message.document.file_id if message.document else None,
    )

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
