# print(1.2345e-3)

# a = int(input())
# b = int(input())
# print(int(- 1.6))
# a = 9**19
# print(a - int(float(9**19)))


# x = int(input())
# h = int(input())
# m = int(input())
#
# print((x + (h*60) + m) // 60)
# print((x + (h*60) + m ) % 60)

"""
#Високосный или обычный год

a = int(input("Введите год: "))
b = a % 4 == 0 and a % 100 != 0 or a % 400 == 0
c = a % 400 == 0

if 1900 <= a <= 3000:
    if b is True:
        print(f"Введённый вами {a} год, является - Високосный!")
    else:
        print(f"Введённый вами {a} год, является - Обычный!")
"""

""" #Площадь треугольника по Герону

a = int(input("Введите длину стороны треугольника 'a': "))
b = int(input("Введите длину стороны треугольника 'b': "))
c = int(input("Введите длину стороны треугольника 'c': "))

p = (a + b + c) / 2
s = p * (p - a) * (p - b) * (p - c)
s **= 0.5
print(f"Площадь треугольника по указанным выше длинам трёх его сторон по формуле Герона, ровна: {s}")
"""

'''
#Не правильно рабочий код

a = int(input())

if a not in range(-14, 13) and not range(15, 16) and not range(19, ):
    print("False")
else:
    print("True")
'''

"""
#Если число входит в условия, тогда True, если нет False.

a = int(input())
print(((-15 < a <= 12) or (14 < a < 17) or (19 <= a)))


# a = int(input())
# if (-15 < a <= 12) or (14 < a < 17) or (19 <= a):
#     print ('True')
# else:
#     print ('False')

"""

"""
# Простейший калькулятор

a = float(input("Введите первое число: "))
b = float(input("Введите первое число: "))
x = input("Введите знак '+, -, /, *': ")

if (x == "mod" or x == "div" or x == "/") and (b == 0):
    print("Деление на 0!")
else:
    if x == "+":
        print(a + b)
    elif x == "-":
        print(a - b)
    elif x == "/":
        print(a / b)
    elif x == "*":
        print(a * b)
    elif x == "mod":
        print(a % b)
    elif x == "pow":
        print(a ** b)
    elif x == "div":
        print(a // b)
"""

"""
# Вычесление площади(Круга, Треугольника, Прямоугольника)
triangle_cirkle_ractangle = input("Введите тип фигуры комнаты и соответствующие параметры 
(треугольник, прямоугольник или круг): ")

if triangle_cirkle_ractangle == "треугольник":
    a = float(input("Введите длину стороны треугольника 'a': "))
    b = float(input("Введите длину стороны треугольника 'b': "))
    c = float(input("Введите длину стороны треугольника 'c': "))
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    s **= 0.5
    print(f"Площадь треугольника ровна: {s}")
elif triangle_cirkle_ractangle == "прямоугольник":
    a = float(input("Введите длину: "))
    b = float(input("Введите ширину: "))
    s = a * b
    print(f"Площадь прямоугольника ровна: {s}")
elif triangle_cirkle_ractangle == "круг":
    pi = 3.14
    r = float(input("Введите радиус: "))
    s = pi * r ** 2
    print(f"Площадь круга ровна: {s}")
"""

"""
#Ввести 3 числа выведет max - min и то что останется
a = int(input())
b = int(input())
c = int(input())
x = a + b + c
min_number = min(a, b, c)
max_number = max(a, b, c)
midlle_number = x - (min_number + max_number)

print(max(a, b, c))
print(min(a, b, c))
print(midlle_number)
"""

"""

#Пишет кол-во програмистов с правильным окончанием


n = int(input("Введите число: "))

list_sta_4 = [14,114,214, 314, 514, 614, 714, 714, 814, 914]
list_sta_3 = [13, 113, 213, 313, 413, 513, 613, 713, 813, 913]
list_sta_2 = [12, 112, 212, 312 ,412, 512, 612, 712, 812, 912]
list_st_1 = [11, 111, 211, 311, 411, 511, 611, 711, 811, 911]

if 0 <= n <= 1000:

    if (n % 10 == 1) and (n not in list_st_1):
        print(f"{n} программист")
    elif (n % 10 == 2 and n not in list_sta_2) or 
    (n % 10 == 4 and n not in list_sta_4) or 
    (n % 10 == 3 and n not in list_sta_3):
        print(f"{n} программиста")
    else:
        print(f"{n} программистов")


n = int(input("Введите число: "))

if 0 <= n <= 1000:

    if n % 10 == 1 and n % 100 != 11:
        print(f"{n} программист")
    elif 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        print(f"{n} программиста")
    else:
        print(f"{n} программистов")
        
"""

"""
# Счастливый или Обычный билет

tic_num = input("Введите 6-ти значный номер билета: ")
first_half_numb = int(tic_num[0]) + int(tic_num[1]) + int(tic_num[2])
second_half_numb = int(tic_num[3]) + int(tic_num[4]) + int(tic_num[5])


if len(tic_num) == 6:
    if first_half_numb == second_half_numb:
        print(f"Ваш билет с номером {tic_num} - Счастливый!!!")
    else:
        print(f"Ваш билет с номером {tic_num} - Обычный!!!")
else:
    print(f"Вы ввели не правильное количество цифр!!!")
    """

"""
# Программа которая суммируе последователно каждкю цифру 
a = int(input())
b = int(input())
summa = 0
i = a
while i <= b:
    summa += i
    i += 1
print(summa)
"""

"""
#Напишите программу, которая считывает со стандартного ввода целые числа,
 по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.

numbers = ()
s = 0

while numbers != 0:
    numbers = int(input("Введите число: "))
    s += int(numbers)
    if numbers == 0:
        print(s)
"""

"""
# В Институте биоинформатики между информатиками и биологами устраивается соревнование.
 Победителям соревнования достанется большой и вкусный пирог. 
 В команде биологов 'a' человек, а в команде информатиков — 'b' человек.
 Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде,
  выигравшей соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. 
  И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.
 Напишите программу, которая помогает найти это число.
 Программа должна считывать размеры команд (два положительных целых числа a и b,
  каждое число вводится на отдельной строке) и выводить наименьшее число d, 
  которое делится на оба этих числа без остатка.
a = int(input())
b = int(input())
d = 1

while d % a != 0 or d % b != 0:
    d += 1
print(d)
"""

# while True:
#     num = int(input())
#     if num < 10:
#         continue
#     if num > 100:
#         break
#     else:
#         print(num)

"""
# Програмка которая создаёт таблицу умножения из введённых чисел
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for o in range(c, d + 1):
    print(end='\t')
    print(o, end='')
print()
for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
    print()
    
"""

"""
Три разных примера, но результат одинаковый. Перебирать диапазон вводимых чисел через пробел
и складывать, только не чётные числа, затем вывести результат.
#1)a, b = input().split()
a = int(a)
b = int(b)
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    s += i
print(s)

#2) a, b = input().split()
a = int(a)
b = int(b)
s = 0
for i in range(a, b + 1, 2):
    if a % 2 == 1:
        s += i
print(s)
#3) a, b = (int(i) for i in input().split())
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    s += i
print(s)

"""




