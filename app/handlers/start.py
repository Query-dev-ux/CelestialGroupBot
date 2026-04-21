from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from app.texts.start import START_TEXT
from app.keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):

    photo = FSInputFile("app/assets/start.png")
    await state.clear()
    await message.answer_photo(photo=photo, caption=START_TEXT, reply_markup=main_menu())
