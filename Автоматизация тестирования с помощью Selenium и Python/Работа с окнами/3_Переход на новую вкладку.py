# coding: utf8
"""
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и
решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
1. Нажать на кнопку
2. Переключиться на новую вкладку
3. Пройти капчу для робота и получить число-ответ

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с
числом. Отправьте полученное число в качестве ответа на это задание.
"""
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url_page_1 = 'https://suninjuly.github.io/redirect_accept.html'
driver = webdriver.Chrome()


def calc(num_x):
    return str(math.log(abs(12 * math.sin(int(num_x)))))


try:
    driver.get(url_page_1)
    button_1 = driver.find_element(By.CSS_SELECTOR, 'button.trollface')
    button_1.click()  # После нажатия кнопки, в браузере появляется вторая вкладка
    sleep(1)

    url_page_2 = driver.window_handles[1]  # Забираем ссылку второй вкладки
    driver.switch_to.window(url_page_2)  # Переходим на вторую страницу
    sleep(2)

    number_x = driver.find_element(By.XPATH, "//div[@class='form-group']//div[@class='form-group']//span[2]").text
    answer_input = driver.find_element(By.CSS_SELECTOR, "input[id='answer']")
    answer_input.send_keys(calc(number_x))

    button_2 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_2.click()


finally:
    sleep(4)
    driver.quit()

    