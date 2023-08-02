"""Helper functions for retrieving data from files
and processing information from handlers and keyboards.
"""

from aiogram.types import CallbackQuery

import copy
import json


def get_faq_sections() -> dict[str, dict[str, dict[str, str]]]:
    """Retrieves sections and questions from the faq.json"""
    with open('lexicon/faq.json', 'r', encoding='utf-8') as f:
        sections: dict[str, dict[str, dict[str, str]]] = json.load(f)['sections']
    return sections


def get_tours_list() -> dict[str, dict[str, str]]:
    """Retrieves the list of all tours from the tours_list.json"""
    with open('lexicon/tours_list.json', 'r', encoding='utf-8') as f:
        tours: dict[str, dict[str, str]] = json.load(f)['tours']
    return tours


def get_group_tours_list():
    """Retrieves the list of group tours from the overall list of all tours"""
    all_tours: dict = get_tours_list()
    group_tours: dict = {}
    for key, value in all_tours.items():
        if value['is_group_tour']:
            group_tours[key] = value
    return group_tours


def get_private_tours_list():
    """Retrieves the list of private tours from the overall list of all tours"""
    all_tours: dict = get_tours_list()
    private_tours: dict = {}
    for key, value in all_tours.items():
        if not value['is_group_tour']:
            private_tours[key] = value
    return private_tours


def get_tour_specs(callback: str | CallbackQuery) -> dict:
    """Retrieves the tour specifications by its name from the list of all tours"""
    tour_specs: dict = get_tours_list()[callback]
    return tour_specs


def cut_tour_specs_for_keyboard(user_dict: dict) -> dict:
    """Processes the dictionary containing information about tour specifications
    for use in an inline keyboard"""
    specs: dict = copy.deepcopy(user_dict)
    for key in ['is_group_tour', 'Название', 'О чём экскурсия?']:
        specs.pop(key, None)
    return specs
