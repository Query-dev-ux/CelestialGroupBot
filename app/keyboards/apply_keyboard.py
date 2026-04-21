from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def apply_keyboard():
    """Кнопка назад к вакансии (под формой отклика на конкретную вакансию)."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_vac")],
    ])


def send_cv_keyboard():
    """Кнопка назад к списку (под формой общего резюме)."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_vacancies")],
    ])
