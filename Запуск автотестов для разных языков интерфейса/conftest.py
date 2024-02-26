from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# user_language = ['gb-en', 'fr']
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome(default) or firefox')
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language: --language=ru or --language=en-gb or --language=fr')


@pytest.fixture()
def browser(request):

    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == 'chrome':
        chrome_option = Options()
        chrome_option.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_option)

    elif browser_name == 'firefox':
        firefox_option = Options()
        firefox_option.add_argument('--incognito')
        firefox_option.set_preference('intl.accept_languages', user_language)

        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_option)

    yield driver
    sleep(3)
    driver.quit()



