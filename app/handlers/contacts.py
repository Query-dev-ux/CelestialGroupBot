from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.texts.contacts import CONTACTS_TEXT
from app.keyboards.contacts_menu import contacts_keyboard
from app.utils.bot_msg import edit_or_replace, safe_delete

router = Router()


@router.message(F.text == "Контакты")
async def contacts_handler(message: Message, state: FSMContext, bot: Bot):
    await safe_delete(message)
    await state.set_state(None)
    await edit_or_replace(bot, message.chat.id, state, CONTACTS_TEXT, reply_markup=contacts_keyboard(), parse_mode=None)
