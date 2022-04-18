"""
Test case #2:
1. Check if there is a 'Картинки' on a page
2. Check if you go to a 'https://yandex.ru/images/' url
3. Check if open first category, check text in a search field.
4. Check if open first picture, check if its opens.
______________________________________________________
Use ▶ to start.
Before start, make sure you have requirements installed (use 'pip install -r requirements.txt' command in terminal)
"""

import pytest
from pages.yandex import MainPage
from selenium.webdriver.common.by import By


# Check if there are 'Картинки' on a page
def test_search_pictures(setup):
    page = MainPage(setup)
    yandex_images = page.images

    assert yandex_images is not None, 'Категория "Картинки" не найдена'

    # Check if you go to 'https://yandex.ru/images/' url
    images_link = page.images
    images_link.click()

    page.wait_page_loaded()

    setup.switch_to.window(setup.window_handles[1])

    current_url = page.get_current_url()
    expected_url = 'https://yandex.ru/images/'

    assert current_url == expected_url, f'Ожидаемый {expected_url} URL не совпадает с найденным {current_url}'


def test_search_pictures_continue(setup):
    page = MainPage(setup)
    images_link = page.images
    images_link.click()
    page.wait_page_loaded()
    setup.switch_to.window(setup.window_handles[1])

    # Check if open first category, check text in a search field.
    categories = page.images_categories
    items = [elem.text.strip().split('\n') for elem in categories[:1]]
    category_name = items[0]
    category = categories[0]
    category_link_from_picture = setup.find_element(By.CSS_SELECTOR, '.PopularRequestList>div>a').get_attribute('href')

    category.click()

    page.wait_page_loaded()
    category_link_actual = page.get_current_url()

    assert category_link_from_picture == category_link_actual, f'Ожидаемая ссылка на {category_name} - ' \
                                                               f'{category_link_from_picture} не совпадает с ' \
                                                               f'реальной {category_link_actual}. '

    # Check if open first picture, check if its opens.
    image_preview = setup.find_element(By.CSS_SELECTOR, '.serp-item__preview')
    image_preview.click()

    assert image_preview is not None, 'Картинка не открывается'

    first_image = setup.find_element(By.CSS_SELECTOR, '.MMImage-Origin')
    first_image_url = first_image.get_attribute('src')

    forward_button = page.forward_button
    forward_button.click()
    page.wait_page_loaded()

    second_image = setup.find_element(By.CSS_SELECTOR, '.MMImage-Origin')
    second_image_url = second_image.get_attribute('src')

    backward_button = page.backward_button
    backward_button.click()
    page.wait_page_loaded()

    image_to_check = setup.find_element(By.CSS_SELECTOR, '.MMImage-Origin')
    image_to_check_url = image_to_check.get_attribute('src')

    assert (first_image_url == image_to_check_url), 'Ошибка при переходе на другую картинку'
