# coding: utf8
"""
Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать
несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим
сценарием действий:

1. открыть страницу
2. авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
3. ввести правильный ответ (поле перед вводом должно быть пустым)
4. нажать кнопку "Отправить"
5. дождаться фидбека о том, что ответ правильный
6. проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
Опциональный фидбек — это текст в черном поле, как показано на скриншоте.


Правильным ответом на задачу в заданных шагах является число:
import time
import math
answer = math.log(int(time.time()))


Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:
https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1

Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты работали
стабильно.

В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со
строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.

Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено правильное локальное время
(https://time.is/ru/). Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают.

"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Password import login, password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

links_list = ['https://stepik.org/lesson/236895/step/1',
              'https://stepik.org/lesson/236896/step/1',
              'https://stepik.org/lesson/236897/step/1',
              'https://stepik.org/lesson/236898/step/1',
              'https://stepik.org/lesson/236899/step/1',
              'https://stepik.org/lesson/236903/step/1',
              'https://stepik.org/lesson/236904/step/1',
              'https://stepik.org/lesson/236905/step/1']


# link = 'https://stepik.org/lesson/236895/step/1'


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize('link', links_list[::-1])
def test_authorization(driver, link):
    driver.get(link)
    wait = WebDriverWait(driver, 20)
    driver.implicitly_wait(15)

    login_button = wait.until(
        EC.visibility_of_element_located((By.ID, 'ember33'))
    )
    login_button.click()
    print('\nНажата кнопка Войти')

    log_in = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='login']")))
    log_in.send_keys(login)
    print('Введён логин')

    pass_word = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    pass_word.send_keys(password)
    print('Введён password')

    driver.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
    print('Нажата кнопка Войти, после введённых данных')

    try:
        solve_again_button = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.again-btn'))
        )
        solve_again_button.click()
        try:
            alert = wait.until(EC.alert_is_present())
            alert.send_keys(u'\ue007')

            # wait.until(EC.element_to_be_clickable((By.XPATH, "//footer[@id = 'ember525']/button[1]"))).click()
        except:
            print('Всплывающего окна нету')
    except:
        print('Нету кнопки "Solve again"')

    finally:
        text_area = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea.string-quiz__textarea'))
        )
        answer = math.log(int(time.time()))

        text_area.send_keys(answer)
        print('Введён ответ')

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    ).click()
    print('Нажата кнопка Submit, после введённых данных')

    feedback = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
    ).text

    assert feedback == 'Correct!', f'Feedback not {feedback}'


"""

pytest -s -v test_paramatrize_Задание_параметризация_тестов.py

"""
