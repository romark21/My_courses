import time

import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_button_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    # with pytest.raises(NoSuchElementException):
    browser.implicitly_wait(3)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket').is_enabled()

    print(browser.current_url)
    assert button is True, "That button doesn't exist"
    # pytest.fail("That button doesn't exist")


