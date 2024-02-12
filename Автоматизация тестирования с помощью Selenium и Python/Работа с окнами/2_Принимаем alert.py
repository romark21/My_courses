# coding: utf8
"""
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

1. Открыть страницу http://suninjuly.github.io/alert_accept.html
2. Нажать на кнопку
3. Принять confirm
4. На новой странице решить капчу для роботов, чтобы получить число с ответом

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с
числом. Отправьте полученное число в качестве ответа на это задание.
"""
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def calc(num_x):
    return str(math.log(abs(12 * math.sin(int(num_x)))))


url_page_1 = 'http://suninjuly.github.io/alert_accept.html'
driver = webdriver.Chrome()

try:
    driver.get(url_page_1)

    button_1 = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button_1.click()
    sleep(2)

    driver.switch_to.alert.accept()  # Нажимаем "Ок" в сплывающем окне. Затем, происходит Redirect на другую страницу.

    number_x = driver.find_element(By.ID, "input_value").text
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(calc(number_x))

    button_2 = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button_2.click()

finally:
    sleep(4)
    driver.quit()

