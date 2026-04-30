from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def contacts_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="HRD: @ira_celestial", url="https://t.me/ira_celestial")],
        [InlineKeyboardButton(text="Партнеры: @bizdev_celestial", url="https://t.me/bizdev_celestial")],
        [InlineKeyboardButton(text="⬅️ Главное меню", callback_data="back_main_menu")],
    ])
