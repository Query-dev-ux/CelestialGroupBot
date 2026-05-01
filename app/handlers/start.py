from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from app.texts.start import START_TEXT
from app.keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    old_msg_id = data.get("bot_msg_id")
    await state.clear()

    if old_msg_id:
        try:
            await bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=old_msg_id,
                text=START_TEXT,
                reply_markup=main_menu(),
            )
            await state.update_data(bot_msg_id=old_msg_id)
            return
        except Exception:
            try:
                await bot.delete_message(message.chat.id, old_msg_id)
            except Exception:
                pass

    sent = await bot.send_message(
        chat_id=message.chat.id,
        text=START_TEXT,
        reply_markup=main_menu(),
    )
    await state.update_data(bot_msg_id=sent.message_id)


@router.callback_query(F.data == "back_main_menu")
async def back_main_menu_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(None)
    await callback.message.edit_text(START_TEXT, reply_markup=main_menu())
    await callback.answer()
