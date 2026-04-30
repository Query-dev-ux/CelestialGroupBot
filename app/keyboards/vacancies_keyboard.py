from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def vacancies_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Senior Media Buyer (iGaming)", callback_data="vac_senior")],
        [InlineKeyboardButton(text="Media Buyer (Facebook)", callback_data="vac_fb")],
        [InlineKeyboardButton(text="Media Buyer (Google)", callback_data="vac_google")],
        [InlineKeyboardButton(text="SEO Specialist", callback_data="vac_seo")],
        [InlineKeyboardButton(text="HR Assistant", callback_data="vac_hr")],
        [InlineKeyboardButton(text="Business Development Manager (iGaming)", callback_data="vac_bizdev")],
        [InlineKeyboardButton(text="Affiliate Manager (iGaming)", callback_data="vac_affiliate")],
        [InlineKeyboardButton(text="Отправить резюме", callback_data="send_cv")],
        [InlineKeyboardButton(text="⬅️ Главное меню", callback_data="back_main_menu")],
    ])
