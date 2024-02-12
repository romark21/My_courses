# coding: utf8
"""
В этом задании в форме регистрации требуется загрузить текстовый файл.
Напишите скрипт, который будет выполнять следующий сценарий:

1. Открыть страницу http://suninjuly.github.io/file_input.html
2. Заполнить текстовые поля: имя, фамилия, email
3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4. Нажать кнопку "Submit"

Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого
задания.

"""


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://suninjuly.github.io/file_input.html'
driver = webdriver.Chrome()

try:
    driver.get(url)
    sleep(2)

    first_name = driver.find_element(By.CSS_SELECTOR, "div.form-group input[name='firstname']")
    first_name.send_keys('Вася ')

    last_name = driver.find_element(By.XPATH, "//input[@type='text'][2]")
    last_name.send_keys('Пупкин')

    email = driver.find_element(By.NAME, 'email')
    email.send_keys('vasjapupkin@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # Получили путь до директории
    file_path = os.path.join(current_dir, '5_Загрузка файлов.txt')  # Добавили имя файла, получили полный путь
    send_file = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    send_file.send_keys(file_path)

    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()


finally:
    sleep(4)
    driver.quit()

"""

print(os.path.abspath(__file__))  #Получам полный путь до тякущего исполняемого файла.

print(os.path.abspath(os.path.dirname(__file__)))  #Получам путь только до директории тякущего исполняемого файла.

"""
