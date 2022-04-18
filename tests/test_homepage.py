"""
Test case #1:
1. Check if there is a search field on a page
2. Check if you can get suggestions after typing text
3. Check if you get result table after press Enter
4. Check if you can find 'tensor.ru' in top-5 results
______________________________________________________
Use ▶ to start.
Before start, make sure you have requirements installed (use 'pip install -r requirements.txt' command in terminal)
"""

import pytest
from pages.yandex import MainPage


# Check if input field is available
def test_search_text(setup):
    page = MainPage(setup)
    input_field = page.search

    assert input_field is not None, 'No input field found on a page'


# Check if suggestions are available
    page.search = 'Тензор'
    page.search_run_button.click()
    suggests = page.suggest_table

    assert suggests is not None, 'No suggests found on a page'


# Check if there is a result table after search
    link_to_search = 'tensor.ru'
    table = page.result_table

    assert table is not None, 'No results table found on a page'


# Check if there is 'Тензор' in top-5 suggestions
    items = [elem.text.strip().split('\n') for elem in table[:5]][0]

    assert link_to_search in items, f'{link_to_search} is not in top-5 results'