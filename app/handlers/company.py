from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.texts.company import COMPANY_TEXT
from app.keyboards.main_menu import back_main_menu_keyboard

router = Router()


@router.callback_query(F.data == "menu_company")
async def company_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(None)
    await callback.message.edit_text(COMPANY_TEXT, reply_markup=back_main_menu_keyboard(), parse_mode="HTML")
    await callback.answer()
