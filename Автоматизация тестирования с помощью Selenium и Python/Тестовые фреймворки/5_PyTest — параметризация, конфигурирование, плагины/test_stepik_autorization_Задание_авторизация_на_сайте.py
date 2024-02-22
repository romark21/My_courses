# coding: utf8

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Password import login, password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
Для следующей задачи вам необходимо авторизоваться на stepik со своим логином и паролем. Пожалуйста, будьте внимательны 
и не добавляйте свои логин и пароль в публичные репозитории на GitHub. 

Ваша задача -- реализовать автотест со следующим набором действий:

открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
авторизоваться со своими логином и паролем 
дождаться того, что поп-апа с авторизацией больше нет
После того как авторизация успешно пройдет, переходите к следующему шагу. 

Запуск из терминала:
pytest -s -v test_stepik_autorization_Задание_авторизация_на_сайте.py

"""


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_authorization(driver):
    link = 'https://stepik.org/lesson/236895/step/1'
    driver.get(link)

    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'ember33'))
    )
    login_button.click()

    log_in = driver.find_element(By.CSS_SELECTOR, "input[name='login']")
    log_in.send_keys(login)

    pass_word = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    pass_word.send_keys(password)

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    submit_button.click()
    sleep(10)
