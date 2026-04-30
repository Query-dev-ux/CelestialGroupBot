from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="О компании", callback_data="menu_company")],
        [InlineKeyboardButton(text="Открытые вакансии", callback_data="menu_vacancies")],
        [InlineKeyboardButton(text="Контакты", callback_data="menu_contacts")],
    ])


def back_main_menu_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Главное меню", callback_data="back_main_menu")],
    ])
