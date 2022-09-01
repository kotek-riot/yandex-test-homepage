# yandex-test-homepage

This is a file to test Yandex main page and pictures search page.

You can find test cases in tests directory. 

Use ▶ to start.
Before start, make sure you have requirements installed 
(use 'pip install -r requirements.txt' command in terminal).

For these test cases, I use Chrome + Yandex.

Make sure, you have a chromedriver installation file on your computer.
If not, download it from: https://chromedriver.chromium.org/downloads

Check file path in 26-th line in conftest.py, it has to be the same, as the path you used for saving your chromedriver.exe

_____________
Test case #1:
1. Check if there is a search field on a page
2. Check if you can get suggestions after typing text
3. Check if you get result table after press Enter
4. Check if you can find 'tensor.ru' in top-5 results
_____________
Test case #2:
1. Check if there is a 'Картинки' on a page
2. Check if you go to a 'https://yandex.ru/images/' url
3. Check if open first category, check text in a search field.
4. Check if open first picture, check if its opens.

________________________________________________________________________________________________________

Это программа для автотеста главной страницы Яндекса.
В папке tests находятся тесты для проверки. 

Use ▶ to start.
Используйте ▶ для запуска.
Перед началом убедитесь в том, что установлены требуемые библиотеки.
(команда 'pip install -r requirements.txt').

Для тестов использован браузер Chrome и сайт Яндекс.

Установочник chromedriver: https://chromedriver.chromium.org/downloads

В conftest.py на 26 линии должен быть тот же путь, по которому лежит chromedriver.exe.

_____________
Тест #1:
1. Есть ли поле поиска на странице
2. Появляются ли подсказки при поиске
3. Появляется ли таблица результатов после Enter
4. Есть ли "tensor.ru" в первых пяти результатах поиска
_____________
Тест #2:
1. Есть ли 'Картинки' на странице
2. Проверить переход по ссылке 'https://yandex.ru/images/'
3. Проверить переход на первую категорию в поиске, текст в поле поиска
4. Проверить кликабельность картинок и переход между ними
