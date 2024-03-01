# coding: utf8
"""
                                    Задание №1
  Написать программу, которая принимает на вход два целых числа (a и b) и совершает с ними следующие действия:
- сравнивает эти два числа и возвращает результат сравнения путем вывода в консоль одного из вариантов:
"a > b", "a < b" или "a = b";

- совершает с этими числами операции сложения, вычитания, деления и умножения и результат выводит в консоль.

                                      Задание №2
  Написать программу, которая принимает на вход две строки (a и b) и сравнивает их. В результате сравнения в консоль
должно быть выведено одно из сообщений: "Строки неидентичны" или "Строки идентичны"


                                      Задание №3
Задан массив целых чисел: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Необходимо написать программу, которая выведет в консоль все
чётные числа.
"""


# Запустить код, затем следовать командам в консоли.


def compares_two_numbers(a, b):
    if a > b:
        return f'{a} > {b}'
    elif a < b:
        return f'{a} < {b}'
    else:
        return f'{a} = {b}'


def additions_numbers(a, b):
    return f'{a} + {b} = {a + b}'


def subtraction_numbers(a, b):
    return f'{a} - {b} = {a - b}'


def division_numbers(a, b):
    return f'{a} : {b} = {a / b}'


def multiplication_numbers(a, b):
    return f'{a} * {b} = {a * b}'


def compares_two_strings(string_1, string_2):
    if string_1 == string_2:
        return 'Строки идентичны!'
    else:
        return 'Строки неидентичны!'


def even_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return (num for num in numbers if num % 2 == 0)


def run_code():
    separate = '----' * 30
    choice_of_task = int(input('Какое задание вы хотите выполнить?:\n'
                               '1 - Задание №1\n'
                               '2 - Задание №2\n'
                               '3 - Задание №3\n'
                               'Введите номер команды: '))
    print(separate)
    if choice_of_task == 1:

        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))

        print(compares_two_numbers(a, b))
        print(additions_numbers(a, b))
        print(subtraction_numbers(a, b))
        print(division_numbers(a, b))
        print(multiplication_numbers(a, b))

    elif choice_of_task == 2:
        string_1 = input('Введите первую строку: ')
        string_2 = input('Введите вторую строку: ')
        print(compares_two_strings(string_1, string_2))

    elif choice_of_task == 3:
        print(f'Чётными числами являются:', *even_numbers())
    else:
        print('Такой команды нет! Введите: 1, 2 или 3')


run_code()




