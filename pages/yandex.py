from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements
from selenium.webdriver.common.by import By


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://yandex.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='text')

    # Run search button
    search_run_button = WebElement(css_selector='.search2__button')

    # Search suggest table
    suggest_table = WebElement(css_selector='.mini-suggest__popup.mini-suggest__popup_theme_tile.mini'
                                            '-suggest__popup_visible')

    # Search images
    images = WebElement(xpath='//a[@data-id="images"]')

    # Search result table
    result_table = ManyWebElements(xpath='//ul[@id="search-result"]')

    # Search result link
    result_links = ManyWebElements(css_selector='#search-result>li>div>h2>a')

    # Search images categories
    images_categories = ManyWebElements(css_selector='.PopularRequestList>div')

    # Image view
    image_view = WebElement(css_selector='.MMImage-Origin')

    # Forward button
    forward_button = WebElement(
        css_selector='.CircleButton.CircleButton_type_next.CircleButton_type.MediaViewer-Button')

    # Backward button
    backward_button = WebElement(
        css_selector='.CircleButton.CircleButton_type_prev.CircleButton_type.MediaViewer-Button')
