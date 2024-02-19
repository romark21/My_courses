# coding: utf8
"""
Отметить тест как падающий

Теперь добавим в наш тестовый класс тест, который проверяет наличие кнопки "Избранное":

def test_guest_should_see_search_button_on_the_main_page(self, browser):
     browser.get(link)
     browser.find_element(By.CSS_SELECTOR, "button.favorite")

Предположим, что такая кнопка должна быть, но из-за изменений в коде она пропала. Пока разработчики исправляют баг,
мы хотим, чтобы результат прогона всех наших тестов был успешен, но падающий тест помечался соответствующим
образом, чтобы про него не забыть. Добавим маркировку @pytest.mark.xfail для падающего теста.

test_fixture10_XFail_помечать_тест_как_ожидаемо_падающий.py:

"""

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#
#     @pytest.mark.xfail
#     def test_guest_should_see_search_button_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "button.favorite")


"""
Запустим наши тесты:

pytest -v test_fixture10_XFail_помечать_тест_как_ожидаемо_падающий.py
Наш упавший тест теперь отмечен как xfail, но результат прогона тестов помечен как успешный:

Когда баг починят, мы это узнаем, так как теперь тест будет отмечен как 
XPASS (“unexpectedly passing” — неожиданно проходит). После этого маркировку xfail для теста можно удалить. 
Кстати, к маркировке xfail можно добавлять параметр reason. Чтобы увидеть это сообщение в консоли, при запуске нужно 
добавлять параметр pytest -rx.

test_fixture10_XFail_помечать_тест_как_ожидаемо_падающий.py:
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")


"""
Запустим наши тесты:

pytest -rx -v test_fixture10_XFail_помечать_тест_как_ожидаемо_падающий.py
 
Сравните вывод в первом и во втором случае.
XPASS-тесты
Поменяем селектор в последнем тесте, чтобы тест начал проходить.

test_fixture10_XFail_помечать_тест_как_ожидаемо_падающий.py:
"""

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# class TestMainPage1():
#
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#
#     @pytest.mark.xfail(reason="fixing this bug right now")
#     def test_guest_should_see_search_button_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")


"""
Запустите тесты. Здесь мы добавили символ X в параметр -r, чтобы получить подробную информацию по XPASS-тестам:

pytest -rX -v test_fixture10_XFail_помечать_тест_как_ожидаемо_падающий.py
И изучите отчёт: 

Дополнительно об использовании этих меток можно почитать в документации: Skip and xfail: dealing with tests that 
cannot succeed.  
Там есть много разных интересных особенностей, например, как пропускать тест только при выполнении условия, 
как сделать так, чтобы внезапно прошедший xfailed тест в отчете стал красным, и так далее.
"""
