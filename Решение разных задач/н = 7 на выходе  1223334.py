
"""Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько
элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных
через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4."""

num = int(input())
count = 0

for i in range(1, num + 1):
    a = 0
    b = i

    while a < b and count != num:
        a += 1
        count += 1
        print(i, end=" ")