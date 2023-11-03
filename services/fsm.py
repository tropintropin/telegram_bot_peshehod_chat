from aiogram.fsm.state import State, StatesGroup


class FSMTourSelection(StatesGroup):
    is_group = State()
    have_children = State()
    kids = State()
    visit = State()
