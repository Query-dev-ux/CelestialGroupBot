from aiogram.fsm.state import StatesGroup, State


class ApplyState(StatesGroup):
    waiting_for_document = State()
