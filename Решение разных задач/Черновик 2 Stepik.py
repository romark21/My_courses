"""
def number_find():
    a = int(input())
    b = int(input())
    s = 0
    x = 0

    for i in range(a, b + 1):
        if i % 3 == 0:

            s += i
            x += 1
    print(s / x)


number_find()
"""

"""
# GC-состав является важной характеристикой геномных последовательностей и определяется как
 процентное соотношение суммы всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной
  последовательности.Напишите программу, которая вычисляет процентное содержание символов
   G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
Например, в строке "acggtgttat" процентное содержание символов G и C равно 4 / 10 * 100 = 40.0,
 где 4 - это количество символов G и C, а 10 -- это длина строки.
 
 # Пример решения 1 ( более длинный)
 
genome = input()
g = (genome.lower().count('g'.lower()))
c = (genome.lower().count('c'.lower()))
print(g)
print(c)
print(len(genome))
print((((g + c)) / len(genome)) * 100)

 # Пример решения 2 ( более короче)

genome = input().lower()
print(((genome.count('g')) + (genome.count('c'))) / len(genome) * 100)
print(len(genome))
print(genome.count('g'))
print(genome.count('c'))

"""

# line = "asdfrt"
# a = "1,2,3,4,5,6,7,9"
# for i in line:
#     print(i, end=", ")


"""
str = input().lower()
c = 0
for i in range(len(str)-1):
    if (str[i] == str[i+1] or str[i] == str[i-1] or (str[i] != str[i+1] and str[i] != str[i-1])):
        c += 1
    if str[i] != str[i+1]:
        print(f"{str[i]}{c}", end='')

        c = 0
print(f"{str[-1]}{c + 1}")
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы 
информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот
 символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную 
последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.


"""

# name = input()
# students = ['Olga', 'Vasja', 'Kolja']
# students += [name]
# students.sort()
#
# print(list(reversed(students)))
# for student in students:
#     print(f"Hello, {student}!")
# if 'Roma' in students:
#     print("Roma is here!")
# else:
#     print("Roma is not here!")
# if 'Vika' not in students:
#     print("Vika not in list!")

# a = [1, 2, 3]
# b = a
# print(b)
# a[1] = 10
# print(b)
# b[0] = 20
# print(b)
# a = [5, 6]
# print(b)
# a = [0 for i in range(5)]
# print(a)
# a = [i * i for i in range(5)]
# print(a)

"""
 Создать список и вывести сумму списка. Цифры писать в строчку через пробел.
 
 
a = [int(i) for i in input().split()]
print(sum(a))


a = [int(i) for i in input().split()]
s = 0
for i in a:
    s += i
print(s)
"""

# a = [int(i) for i in input().split()]
# # a += [1]
#
# for i in range(len(a)-1):
#     if len(a) == 1:
#         print(a)
#
#     if len(a) == 3:
#         summa = a[i+1] + a[i+1]
#         summa = a[i - 1] + a[i - 1]
#         print(summa)
#         break
#     summa = a[i - 1] + a[i + 1]
#     if a[i] == a[0]:
#         summa = a[1] + a[-2]
#     if a[i] == a[-2]:
#         summa = a[i-1] + a[-1]
#         if a[i] == a[i-1]:
#             summa = a[0] + a[-2]
#            # if a[i] == len print(a[0] + a[-2], end='')
#
#     print(summa, end=' ')
#     summa = 0


# print(f'{a[0] + a[-2]}', end='')

# print(range(len(a)-1))

"""Сложение соседних цифр
a = [int(i) for i in input().split()]

if len(a) == 1:
    print(a[0])
else:
    for i in range(len(a)-1):
        s = a[i - 1] + a[i + 1]

        print(s, end=' ')
    print(a[-2] + a[0])
"""

"""a = [int(i) for i in input().split()]
bin_1 = []
bin_2 = []

for i in a:
    if i in bin_1 and i not in bin_2:
        print(i, end=' ')
        bin_2.append(i)
    if i not in bin_1:
        bin_1.append(i)
"""

""" Найти минимальное число из введённого списка цифр
a = [int(i) for i in input().split()]
l = a[0]

for i in a:
    if l > i:
        l = i
print(l)

"""

"""Сапёр
rows, columns, mines = (int(i) for i in input().split())
playground = [[0 for column in range(columns)] for row in range(rows)]
print(*playground, sep='\n')
for mine in (mines):
    row, col = (int(i) - 1 for i in input().split())
    playground[row][col] = - 1

for i in range(rows):
    for j in range(columns):
        if playground[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < rows and 0 <= aj < columns and [ai][aj] == -1:
                        playground[i][j] += 1

for i in range(rows):
    for j in range(columns):
        if playground[i][j] == -1:
            print("*", end="")
        elif playground[i][j] == 0:
            print(".", end="")
        else:
            print(playground[i][j], end="")
    print()
"""

"""
summa_squared = 0
count_numbers_from_user = []
summa_numbers = []
while summa_numbers != 0:
    num = int(input(f"Введите число: "))
    count_numbers_from_user.append(num)
    summa_numbers = sum(count_numbers_from_user)
    summa_squared = num ** 2 + summa_squared
    if summa_numbers == 0:
        print(summa_squared)


c = [int(input())]
while sum(c) != 0:
    c.append(int(input()))
print(sum(i**2 for i in c))
"""

"""
num = int(input())
count = 0

for i in range(1, num + 1):
    a = 0
    b = i

    while a < b and count != num:
        a += 1
        count += 1
        print(i, end=" ")
"""

"""
a, x = [int(i) for i in input().split()], int(input())

if x not in a:
    print("Отсутствует")

for index, elem in enumerate(a):
    if elem == x:
        print(index, end=' ')



a, x = input().split(), input()

if x not in a:
    print("Отсутствует")
else:
    for i in range(len(a)):
        if a[i] == x:
            print(i, end=' ')
"""
# b = (input().split())
# while "end" not in b:
#     b.append(input().split())
# n = list(map(int, input().split()))


# n = []
# end = ()
#
# while 'end' not in end:
#     end = input().split()
#     n.append(end)
# n.pop()
# n = [list(map(int, i))for i in n]
#
# print(n)
# m = []
#
# li, lj = len(n), len(n[0])
# for row in range(li-1):
#     for elem in range(lj-1):
#         m = n[row-1][elem] + n[row+1][elem] + n[row][elem-1] + n[row][elem+1]
#         print(m, end=' ')
#         # if [row][elem] == n[0][2]:
#         #     m =
#
#
#     print(m, end=' ')
#
#     print()

# n = []
# print(n)
# print(end)

"""
# a = [
#     [1, 4, 6, 7],
#     [4, 8, 1, 0],
#     [7, 4, 9, 3]]
# for row in a:
#     for column in row:
#         print(a[row-1] + a[row+1])




    #     print(column, end=' ')
    # print()
"""

matrix = []
while True:
    u = input().split()
    if "end" in u:
        break
    matrix.append([*map(int, u)])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i > len(matrix):
            print(matrix[i - 1][j] + matrix[0][j] + matrix[i][j - 1] + matrix[i][j + 1], end=' ')
            continue
        if j > len(matrix[i]):
            print(matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][0], end=' ')
            continue

        print(matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1], end=' ')
    print()