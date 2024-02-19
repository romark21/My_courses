import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    print('\nStart browser for tests...')
    driver = webdriver.Chrome()
    yield driver
    print('\nQuit browser...')
    driver.quit()


