from aiogram.fsm.state import State, StatesGroup


class FSMTourSelection(StatesGroup):
    """
    Finite State Machine for Tour Selection Form Section.

    State Descriptions:
    - is_group: Choice between group or individual tour.
    - have_children: Presence of children in the tourist group.
    - kids: Age group of accompanying children if any.
    - visit: Indicates if it's the first city visit or not.
    """

    is_group = State()
    have_children = State()
    kids = State()
    visit = State()


class FSMInvinoveritas(StatesGroup):
    lection = State()