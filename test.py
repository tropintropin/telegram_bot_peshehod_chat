import json
from pathlib import Path


def get_tour_selection_form_results():
    file: Path = Path("lexicon/tours_from_selection_form.json")
    with file.open("r", encoding="utf-8") as f:
        results = json.load(f)["tours"]
        return results


# print(get_tour_selection_form_results()["is_group"])

results = get_tour_selection_form_results()

# def iterate_results(dict: dict):
#     for k, v in dict.items():
#         if type(v) is dict:
#             print(v)
#             yield from iterate_results(v)
#         elif type(v) is list and v is not None:
#             print(v)
#             yield v
#         else:
#             yield v

# print(iterate_results(results))

def iterate(dict: dict):
    for k, v in dict.items():
        if type(v) is dict:
            yield iterate(v)
        else:
            yield v

print(list(iterate(results)))