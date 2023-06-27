import json


def get_faq_sections() -> dict[str, dict[str, dict[str, str]]]:
    with open('lexicon/faq.json', 'r', encoding='utf-8') as faq:
        sections: dict[str, dict[str, dict[str, str]]] = json.load(faq)['sections']
    return sections


def get_tours_list() -> dict[str, dict[str, str]]:
    with open('lexicon/tours_list.json', 'r', encoding='utf-8') as tours_list:
        tours: dict[str, dict[str, str]] = json.load(tours_list)['tours']
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


def get_tour_specs(callback: str) -> dict:
    tour_specs: dict = get_tours_list()[callback]
    return tour_specs


# print(get_faq_sections())
# print(get_tours_list())
# print(get_tour_specs('vr_petra_ochami'))
# print(get_group_tours_list())
# print(get_private_tours_list())