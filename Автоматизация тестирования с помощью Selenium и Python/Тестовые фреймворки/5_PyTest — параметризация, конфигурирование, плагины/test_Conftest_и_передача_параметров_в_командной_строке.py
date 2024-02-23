# coding: utf8


"""Встроенная фикстура request может получать данные о текущем запущенном тесте, что позволяет, например, сохранять
дополнительные данные в отчёт, а также делать многие другие интересные вещи. В этом шаге мы хотим показать, как можно
настраивать тестовые окружения с помощью передачи параметров через командную строку.

Это делается с помощью встроенной функции pytest_addoption и фикстуры request. Сначала добавляем в файле conftest
обработчик опции в функции pytest_addoption, затем напишем фикстуру, которая будет обрабатывать переданные в опции
данные. Подробнее можно ознакомиться здесь: https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption

Добавим логику обработки командной строки в conftest.py. Для запроса значения параметра мы можем вызвать команду:

browser_name = request.config.getoption("browser_name")
conftest.py:

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

test_parser.py:"""

link = "http://selenium1py.pythonanywhere.com/"

from selenium.webdriver.common.by import By


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


"""Если вы теперь запустите тесты без параметра, то получите ошибку:
pytest -s -v test_parser.py
_pytest.config.UsageError: --browser_name should be chrome or firefox


Можно задать значение параметра по умолчанию, чтобы в командной строке не обязательно было 
указывать параметр --browser_name, например, так:
parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
Давайте укажем параметр:
pytest -s -v --browser_name=chrome test_parser.py
А теперь запустим тесты на Firefox:

pytest -s -v --browser_name=firefox test_parser.py
Вы должны увидеть, как сначала тесты запустятся в браузере Chrome, а затем — в Firefox."""