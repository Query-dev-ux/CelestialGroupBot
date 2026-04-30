from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.texts.contacts import CONTACTS_TEXT
from app.keyboards.contacts_menu import contacts_keyboard

router = Router()


@router.callback_query(F.data == "menu_contacts")
async def contacts_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(None)
    await callback.message.edit_text(CONTACTS_TEXT, reply_markup=contacts_keyboard())
    await callback.answer()
