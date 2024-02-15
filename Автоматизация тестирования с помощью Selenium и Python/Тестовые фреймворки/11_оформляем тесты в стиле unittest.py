"""
Попробуйте оформить тесты из первого модуля в стиле unittest.

 Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
1. Создайте новый файл
2. Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
3. Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
4. Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
5. Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
6. Запустите получившиеся тесты из файла
7. Просмотрите отчёт о запуске и найдите последнюю строчку
8. Отправьте эту строчку в качестве ответа на это задание

 Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы
использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо
(во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения.

Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке.
"""


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url_1 = 'http://suninjuly.github.io/registration1.html'
url_2 = 'http://suninjuly.github.io/registration2.html'
driver = webdriver.Chrome()


class TestConfirm(unittest.TestCase):
    def test_confirm_message_1(self):

        try:
            driver.get(url_1)

            first_name = driver.find_element(By.CSS_SELECTOR, ".first_block > .first_class > .first")
            first_name.send_keys('Roman')
            time.sleep(1)

            last_name = driver.find_element(By.CSS_SELECTOR, ".first_block > .second_class > .second")
            last_name.send_keys("Pupkin")
            time.sleep(1)

            email = driver.find_element(By.CSS_SELECTOR, ".first_block > .third_class > .third")
            email.send_keys("romanpupkin@gmail.com")
            time.sleep(1)

            submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
            submit_button.click()
            time.sleep(1)

            actual_text = driver.find_element(By.TAG_NAME, 'h1').text
            expected_text = 'Congratulations! You have successfully registered!'

            self.assertEqual(expected_text, actual_text,
                             f'Expected text: {expected_text}, but given {actual_text}')

        finally:
            driver.quit()

    def test_confirm_message_2(self):

        try:
            driver.get(url_2)

            first_name = driver.find_element(By.CSS_SELECTOR, ".first_block > .first_class > .first")
            first_name.send_keys('Roman')
            time.sleep(1)

            last_name = driver.find_element(By.CSS_SELECTOR, ".first_block > .second_class > .second")
            last_name.send_keys("Pupkin")
            time.sleep(1)

            email = driver.find_element(By.CSS_SELECTOR, ".first_block > .third_class > .third")
            email.send_keys("romanpupkin@gmail.com")
            time.sleep(1)

            submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
            submit_button.click()
            time.sleep(1)

            actual_text = driver.find_element(By.TAG_NAME, 'h1').text
            expected_text = 'Congratulations! You have successfully registered!'

            self.assertEqual(expected_text, actual_text,
                             f'Expected text: {expected_text}, but given {actual_text}')

        finally:
            driver.quit()


if __name__ == "__main__":
    unittest.main()

"""
Примет кода из коминтариев:

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUniqueSelectors(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def fill_form(self, link):
        browser = self.driver
        browser.implicitly_wait(5)
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Kesa')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Lisa')
        browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('KL@google.com')

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
        return welcome_text

    def test_registration(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration_bug(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
"""