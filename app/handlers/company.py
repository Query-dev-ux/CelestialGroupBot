from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.texts.company import COMPANY_TEXT
from app.utils.bot_msg import edit_or_replace, safe_delete

router = Router()


@router.message(F.text == "О компании")
async def company_handler(message: Message, state: FSMContext, bot: Bot):
    await safe_delete(message)
    await state.set_state(None)
    await edit_or_replace(bot, message.chat.id, state, COMPANY_TEXT)
