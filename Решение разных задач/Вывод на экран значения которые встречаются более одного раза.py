"""Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
 которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным."""

a = [int(i) for i in input().split()]
bin_1 = []
bin_2 = []

for i in a:
    if i in bin_1 and i not in bin_2:
        print(i, end=' ')
        bin_2.append(i)
    if i not in bin_1:
        bin_1.append(i)



""" Или более короткое решение"""

a, c = [str(i) for i in input().split()], []
for i in a:
    if i not in c and a.count(i) > 1:
        c.append(i)
        print(i, end=' ')