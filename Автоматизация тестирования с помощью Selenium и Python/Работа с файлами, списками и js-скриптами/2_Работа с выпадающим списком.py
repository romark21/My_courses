# coding: utf8
"""
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота,
 чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу https://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
 вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.



Когда ваш код заработает, попробуйте запустить его на странице https://suninjuly.github.io/selects2.html.
 Ваш код и для нее тоже ﻿должен пройти успешно.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
link_1 = 'https://suninjuly.github.io/selects1.html'
link_2 = 'https://suninjuly.github.io/selects2.html'

def summ_of_numbers(a, b):
    return a + b


try:
    driver.get(link_1)
    time.sleep(1)

    number_1 = int(driver.find_element(By.ID, 'num1').text)
    number_2 = int(driver.find_element(By.ID, 'num2').text)
    result = summ_of_numbers(number_1, number_2)

    select = Select(driver.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(result))

    driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(5)

finally:
    driver.quit()





