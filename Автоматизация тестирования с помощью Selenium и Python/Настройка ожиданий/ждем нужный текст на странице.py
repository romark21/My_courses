# coding: utf8
"""
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3. Нажать на кнопку "Book"
4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из
библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from time import sleep

driver = webdriver.Chrome()
url = 'https://suninjuly.github.io/explicit_wait2.html'


def calc(num_x):
    return str(math.log(abs(12 * math.sin(int(num_x)))))


try:
    driver.get(url)

    book = driver.find_element(By.ID, 'book')  # Находим кнопку 'book'

    WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '$100')  # Ждём пока цена будет ровна "$100"
        )

    book.click()  # Нажимаем кнопку 'book'

    value_x = driver.find_element(By.ID, 'input_value').text

    answer = driver.find_element(By.CSS_SELECTOR, "input.form-control")
    answer.send_keys(calc(value_x))

    submit = driver.find_element(By.ID, 'solve')
    submit.click()

finally:
    sleep(4)
    driver.quit()

