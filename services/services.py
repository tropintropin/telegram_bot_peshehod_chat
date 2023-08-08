"""Helper functions for retrieving data from files
and processing information from handlers and keyboards.
"""

import copy
import json


def get_faq_sections() -> dict[str, dict[str, str | dict[str, str]]]:
    """
    Retrieves sections and questions from the 'faq.json' file.
    
    :return: A dictionary containing sections and their associated questions.
    :rtype: dict[str, dict[str, str | dict[str, str]]]
    """
    with open('lexicon/faq.json', 'r', encoding='utf-8') as f:
        sections: dict[str, dict[str, str | dict[str, str]]] = json.load(f)['sections']
    return sections


def cut_faq_section_items(user_dict: dict) -> dict:
    items: dict = copy.deepcopy(user_dict)
    del items['section_name']
    return items


def get_tours_list() -> dict[str, dict[str, str]]:
    """
    Retrieves the list of all tours from the 'tours_list.json' file.

    :return: A dictionary containing all tours with their associated details.
    :rtype: dict[str, dict[str, str]]
    """
    with open('lexicon/tours_list.json', 'r', encoding='utf-8') as f:
        tours: dict[str, dict[str, str]] = json.load(f)['tours']
    return tours


def get_group_tours_list():
    """
    Retrieves the list of group tours from the overall list of all tours.
    
    :return: A dictionary containing group tours and their associated details.
    :rtype: dict
    """
    all_tours: dict = get_tours_list()
    group_tours: dict = {}
    for key, value in all_tours.items():
        if value['is_group_tour']:
            group_tours[key] = value
    return group_tours


def get_private_tours_list():
    """
    Retrieves the list of private tours from the overall list of all tours.

    :return: A dictionary containing private tours and their associated details.
    :rtype: dict
    """
    all_tours: dict = get_tours_list()
    private_tours: dict = {}
    for key, value in all_tours.items():
        if not value['is_group_tour']:
            private_tours[key] = value
    return private_tours


def get_tour_specs(callback: str) -> dict:
    """
    Retrieves the tour specifications by its name from the list of all tours.
    
    :param callback: The name of the tour or a CallbackQuery object containing the name.
    :type callback: str or aiogram.types.CallbackQuery
    :return: A dictionary containing the specifications of the requested tour.
    :rtype: dict
    """
    tour_specs: dict = get_tours_list()[callback]
    return tour_specs


def cut_tour_specs_for_keyboard(user_dict: dict) -> dict:
    """
    Processes the dictionary containing information about tour specifications
    for use in an inline keyboard
    
    This function creates a new dictionary by making a deep copy of the provided 'user_dict'
    and removes specific keys that are not needed for displaying tour information in an inline keyboard.

    :param user_dict: A dictionary containing information about tour specifications.
    :type user_dict: dict
    :return: A modified dictionary suitable for displaying tour information in an inline keyboard.
    :rtype: dict
    """
    specs: dict = copy.deepcopy(user_dict)
    for key in ['is_group_tour', 'Название', 'О чём экскурсия?']:
        specs.pop(key, None)
    return specs
