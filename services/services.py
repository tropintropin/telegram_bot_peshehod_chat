from aiogram.types import CallbackQuery

import json


def get_faq_sections() -> dict[str, dict[str, dict[str, str]]]:
    with open('lexicon/faq.json', 'r', encoding='utf-8') as f:
        sections: dict[str, dict[str, dict[str, str]]] = json.load(f)['sections']
    return sections


def get_tours_list() -> dict[str, dict[str, str]]:
    with open('lexicon/tours_list.json', 'r', encoding='utf-8') as f:
        tours: dict[str, dict[str, str]] = json.load(f)['tours']
    return tours


def get_group_tours_list():
    all_tours = get_tours_list()
    group_tours = {}
    for key, value in all_tours.items():
        if value['is_group_tour']:
            group_tours[key] = value
    return group_tours


def get_private_tours_list():
    all_tours = get_tours_list()
    private_tours = {}
    for key, value in all_tours.items():
        if not value['is_group_tour']:
            private_tours[key] = value
    return private_tours


def get_tour_specs(callback: str | CallbackQuery) -> dict:
    tour_specs: dict = get_tours_list()[callback]
    return tour_specs

