import json
from pathlib import Path
from typing import Any, Dict, List, Union


def get_tour_selection_form_results() -> Dict[str, Union[str, Dict, List[str]]]:
    file: Path = Path("lexicon/tours_from_selection_form.json")
    with file.open("r", encoding="utf-8") as f:
        results = json.load(f)["tours"]
        return results


results = get_tour_selection_form_results()


def get_non_empty_lists(data: Any) -> List[list]:
    """Made with GPT-3.5"""
    if isinstance(data, list):
        # Если переданный объект - список, возвращаем его, если он не пуст
        return [data] if any(data) else []
    elif isinstance(data, dict):
        # Если переданный объект - словарь, рекурсивно вызываем эту же функцию для значений
        return [item for value in data.values() for item in get_non_empty_lists(value)]
    else:
        # Возвращаем пустой список для прочих типов данных
        return []


print(get_non_empty_lists(results))
