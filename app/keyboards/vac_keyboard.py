from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def vac_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Откликнуться", callback_data="apply_vacancy")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_vacancies")],
    ])
