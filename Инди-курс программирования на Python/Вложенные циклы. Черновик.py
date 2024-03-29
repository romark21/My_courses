"""
------------------------------------------------------------------------------------------------------------------
# Ваша задача найти сумму всех четырехзначных натуральных чисел, сумма цифр которых равна 20.
#
# Примерами таких чисел являются 9065, 8129, 7355 и тд. У каждого из указанных чисел сумма цифр равна 20


stack = []
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                rez = [i, j, k, l]
                if sum(rez) == 20:
                    stack.append(int(''.join(map(str, rez))))
print(sum(stack))
------------------------------------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------------------------------------
# В этой задаче вам предстоит построить лесенку из чисел. 
Программа принимает на вход целое положительное число n (n<=15)
# - количество уровней, ваша задача вывести n уровней, в каждом из которых стоят числа от 1 до значения уровня.
# 
# Sample Input 1:
# 
# 2
# Sample Output 1:
# 
# 1
# 1 2
# 
# Sample Input 2:
# 
# 3
# Sample Output 2:
# 
# 1
# 1 2
# 1 2 3


n = int(input())

for i in range(n):
    for j in range(1, i):
        print(j, end=' ')
    print()
------------------------------------------------------------------------------------------------------------------
"""
"""
------------------------------------------------------------------------------------------------------------------
# Напишите программу для построения горизонтальных столбчатых диаграмм с помощью символа звёздочки. 
# 
# Формат ввода
# Несколько натуральных чисел на одной строке.
# 
# Формат вывода
# Несколько чисел на одной строке.
# 
# Sample Input:
# 
# 3 7 1 10 8
# Sample Output:
# 
# ***
# *******
# *
# **********
# ********


n = [*map(int, input().split())]

for i in range(len(n)):
    print('*' * n[i])
    ------------------------------------------------------------------------------------------------------------------
"""

# num_of_items = int(input())
# num_list = [*map(int, input().split())]
# count = 0
#
# for i in range(len(num_list) - 1):
#     for j in range(len(num_list) - 1 - i):
#         if num_list[j] > num_list[j + 1]:
#             num_list.insert(j, num_list.pop(j + 1))
#             count += 1
# print(count)
"""
------------------------------------------------------------------------------------------------------------------
# Фурик очень любит уроки математики, поэтому, в отличие от Рубика, он их не посещает. Но теперь Фурик хочет получить
# хорошую оценку по математике. Для этого Лариса Ивановна, учительница математики, дала ему новое задание.
# Фурик сразу же решил эту задачу, а вы сможете?
# 
# Задана система уравнений:
# 
# 
# 
# Нужно посчитать количество пар целых чисел (a, b) (0 ≤ a, b), которые удовлетворяют системе.
# 
# Входные данные
# 
# В единственной строке заданы два целых числа n, m (1 ≤ n, m ≤ 1000) — параметры системы.
# Числа в строке разделены пробелом.
# 
# Выходные данные
# 
# В единственную строку выведите ответ на задачу.
# 
# Решение youtube patreon boosty
# 
# Sample Input 1:
# 
# 9 3
# Sample Output 1:
# 
# 1
# Sample Input 2:
# 
# 14 28
# Sample Output 2:
# 
# 1
# Sample Input 3:
# 
# 4 20
# Sample Output 3:
# 
# 0


n, m = map(int, input().split())
count = 0

for i in range(n):
    for j in range(m):
        if i ** 2 + j == n and i + j ** 2 == m:
            count += 1
print(count)

    ------------------------------------------------------------------------------------------------------------------
"""

# num_of_items = int(input())
# num_list = [*map(int, input().split())]
# count = 0
#
# for i in range(num_of_items):
#     for j in range(len(num_list[i]) - 1):
#         if num_list[j] > num_list[j + 1]:
#             num_list.insert(j, num_list.pop(j + 1))
#             count += 1
#
# print(count)

# num_of_items = int(input())
# num_list = [*map(int, input().split())]
# count = 0
#
# for i in range(num_of_items):
#     for j in range(len(num_list[i::-1])):
#         if num_list[j] > num_list[j + 1]:
#             num_list.insert(j, num_list.pop(j + 1))
#             count += 1
#
# print(*num_list)

n = int(input())
matrix = []
dig_summ = 0
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(len(matrix)):
    for j in range(len(i)):
        if i == j:
            dig_summ += matrix[i][j]

