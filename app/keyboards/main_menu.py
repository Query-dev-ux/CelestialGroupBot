from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="О компании")],
            [KeyboardButton(text="Открытые вакансии")],
            [KeyboardButton(text="Контакты")],
        ],
        resize_keyboard=True,
        persistent=True
    )