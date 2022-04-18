"""
For these test cases, I use Chrome browser + Yandex Browser
Make sure, you have an installation file on your computer.
If not, download it from: https://chromedriver.chromium.org/downloads
Check file path in 26-th line, it has to be the same, as the path you used for keeping your chromedriver.exe
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if no UX needed
    options.add_argument('--start-maximized')
    #options.add_argument('--window-size=1300,900')  # Set UX window size
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=DEBUG')

    return options


@pytest.fixture
def get_web_browser(get_chrome_options):  # Get browser
    options = get_chrome_options
    service = Service('C:/Windows/chromedriver.exe')  # ChromeDriver file local path
    browser = webdriver.Chrome(service=service, options=options)
    return browser


@pytest.fixture(scope='function')  # Get Yandex Web page
def setup(request, get_web_browser):
    driver = get_web_browser
    driver.set_page_load_timeout(10)
    url = 'https://yandex.ru'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.implicitly_wait(20)
    driver.quit()

