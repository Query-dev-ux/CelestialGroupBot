from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.texts.vacancies import VACANCIES_TEXT, SEND_CV_TEXT, HR_Assistant, Facebook_Media_Buyer, SEO_Specialist, Google_Media_Buyer
from app.texts.apply import HR_Assistant_apply, Facebook_Media_Buyer_apply, SEO_Specialist_apply, Google_Media_Buyer_apply
from app.keyboards.vacancies_menu import vacancies_keyboard
from app.keyboards.vac_keyboard import vac_keyboard
from app.keyboards.apply_keyboard import apply_keyboard, send_cv_keyboard
from app.utils.bot_msg import edit_or_replace, safe_delete
from app.utils.hr import forward_to_hr
from app.states.apply import ApplyState
from app.states.resume import ResumeState

router = Router()

VACANCIES = {
    "vac_hr": {
        "name":       "HR Assistant",
        "text":       HR_Assistant,
        "apply_text": HR_Assistant_apply,
    },
    "vac_fb": {
        "name":       "Media Buyer (Facebook)",
        "text":       Facebook_Media_Buyer,
        "apply_text": Facebook_Media_Buyer_apply,
    },
    "vac_seo": {
        "name":       "SEO Specialist",
        "text":       SEO_Specialist,
        "apply_text": SEO_Specialist_apply,
    },
    "vac_google": {
        "name":       "Media Buyer (Google)",
        "text":       Google_Media_Buyer,
        "apply_text": Google_Media_Buyer_apply,
    },
}


# ── Список вакансий ───────────────────────────────────────────────────────────

@router.message(F.text == "Открытые вакансии")
async def vacancies_handler(message: Message, state: FSMContext, bot: Bot):
    await safe_delete(message)
    await state.set_state(None)
    await edit_or_replace(bot, message.chat.id, state, VACANCIES_TEXT, reply_markup=vacancies_keyboard(), parse_mode=None)


@router.callback_query(F.data == "back_vacancies")
async def back_to_vacancies(callback: CallbackQuery, state: FSMContext):
    await state.set_state(None)
    await callback.message.edit_text(VACANCIES_TEXT, reply_markup=vacancies_keyboard())
    await callback.answer()


# ── Конкретная вакансия ───────────────────────────────────────────────────────

@router.callback_query(F.data.in_(VACANCIES))
async def show_vacancy(callback: CallbackQuery, state: FSMContext):
    vac = VACANCIES[callback.data]
    await state.update_data(current_vac=callback.data)
    await callback.message.edit_text(vac["text"], reply_markup=vac_keyboard(), parse_mode="HTML")
    await callback.answer()


# ── Отклик на конкретную вакансию ─────────────────────────────────────────────

@router.callback_query(F.data == "apply_vacancy")
async def apply_vacancy(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    vac = VACANCIES.get(data.get("current_vac"))
    text = vac["apply_text"] if vac else "Отправь своё резюме!"
    await state.set_state(ApplyState.waiting_for_document)
    await callback.message.edit_text(text, reply_markup=apply_keyboard())
    await callback.answer()


@router.callback_query(F.data == "back_to_vac")
async def back_to_vacancy(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    vac = VACANCIES.get(data.get("current_vac"))
    await state.set_state(None)
    if vac:
        await callback.message.edit_text(vac["text"], reply_markup=vac_keyboard(), parse_mode="HTML")
    else:
        await callback.message.edit_text(VACANCIES_TEXT, reply_markup=vacancies_keyboard())
    await callback.answer()


@router.message(ApplyState.waiting_for_document, F.document | F.text)
async def handle_apply(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    vac = VACANCIES.get(data.get("current_vac"))
    vac_name = vac["name"] if vac else "не указана"
    await state.set_state(None)
    await forward_to_hr(bot, message, state, f"Отклик на вакансию: {vac_name}")


# ── Общее резюме (кнопка «Отправить резюме») ──────────────────────────────────

@router.callback_query(F.data == "send_cv")
async def send_cv(callback: CallbackQuery, state: FSMContext):
    await state.set_state(ResumeState.waiting_for_resume)
    await callback.message.edit_text(SEND_CV_TEXT, reply_markup=send_cv_keyboard())
    await callback.answer()


@router.message(ResumeState.waiting_for_resume, F.document | F.text)
async def handle_send_cv(message: Message, state: FSMContext, bot: Bot):
    await state.set_state(None)
    await forward_to_hr(bot, message, state, "Общий отклик")
