# import pytest
# from selenium import webdriver
#
#
# @pytest.fixture(scope='function')
# def browser():
#     print('\nStart browser for tests...')
#     driver = webdriver.Chrome()
#     yield driver
#     print('\nQuit browser...')
#     driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

user_language = ['en']
def pytest_addoption(parser):

    # По умолчанию запустится chrome
    # parser.addoption('--browser_name', action='store', default="chrome",
    #                  help="Choose browser: chrome or firefox")

    # Всегда нужно указывать в терминале Chrome или Firefox
    # pytest -s -v browser_name=chrome имя файла
    # или
    # pytest -s -v browser_name=firefox имя файла
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'into.accept_languages': user_language})
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

