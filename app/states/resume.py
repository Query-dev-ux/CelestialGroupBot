from aiogram.fsm.state import StatesGroup, State


class ResumeState(StatesGroup):
    waiting_for_resume = State()