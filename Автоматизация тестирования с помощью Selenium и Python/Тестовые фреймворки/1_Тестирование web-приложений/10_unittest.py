# coding: utf8
"""
Тест-раннеры сами находят тестовые методы в указанных при запуске файлах, но для этого нужно следовать общепринятым
правилам. Общее правило для всех фреймворков: название тестового метода должно начинаться со слова "test_".  Дальше
может идти любой текст, который является уникальным названием для теста:

def test_name_for_your_test():
Для unittest существуют собственные дополнительные правила:

Тесты обязательно должны находиться в специальном тестовом классе.
Вместо assert должны использоваться специальные assertion методы.
Давайте теперь изменим наши предыдущие тесты, чтобы их можно было запустить с помощью unittest. Для этого нам
понадобится выполнить следующие шаги:

Импортировать unittest в файл: import unittest
Создать класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента
функции: def test_abs1(self):

Изменить assert на self.assertEqual()
Заменить строку запуска программы на unittest.main()
"""

import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()


"""
После изменений запустим наш файл с тестами всё так же с помощью Python:

python test_abs_project.py

.F

======================================================================

FAIL: test_abs2 (__main__.TestAbs)

----------------------------------------------------------------------

Traceback (most recent call last):

  File "test_abs_project.py", line 9, in test_abs2

    self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

AssertionError: Should be absolute value of a number

----------------------------------------------------------------------

Ran 2 tests in 0.000s

FAILED (failures=1)
Теперь мы видим более подробную информацию о результатах запуска: было запущено два теста, один тест выполнился с 
ошибкой. Место ошибки и пояснение к ней отображаются в логе.

В следующем уроке мы рассмотрим преимущества и особенности использования тестового фреймворка PyTest. Если вы хотите 
использовать unittest в своих проектах, вы можете изучить документацию самостоятельно. 
https://docs.python.org/3/library/unittest.html
"""