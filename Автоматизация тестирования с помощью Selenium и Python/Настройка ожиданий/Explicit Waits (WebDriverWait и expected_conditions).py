# coding: utf8
"""
Чтобы тест был надежным, нам нужно не только найти кнопку на странице, но и дождаться, когда кнопка станет
кликабельной. Для реализации подобных ожиданий в Selenium WebDriver существует понятие явных ожиданий (Explicit Waits),
которые позволяют задать специальное ожидание для конкретного элемента. Задание явных ожиданий реализуется с помощью
инструментов WebDriverWait и expected_conditions. Улучшим наш тест:
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

"""
element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае.

Обратите внимание, что в объекте WebDriverWait используется функция until, в которую передается правило ожидания, 
элемент, а также значение, по которому мы будем искать элемент. В модуле expected_conditions есть много других правил, 
которые позволяют реализовать необходимые ожидания:

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
Описание каждого правила можно найти на сайте.

Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно задать негативное правило с помощью метода until_not:

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    
"""

