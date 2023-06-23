'''Here are the handlers for the FAQ Section.
'''

import json


with open('../lexicon/faq.json', 'r', encoding='utf-8') as faq:
    sections: dict = json.load(faq)['sections']


with open('../lexicon/tours_list.json', 'r', encoding='utf-8') as tours_list:
    tours: dict = json.load(tours_list)['tours']


# print(sections['Оплата и бронирование'].keys())
# print(tours)

