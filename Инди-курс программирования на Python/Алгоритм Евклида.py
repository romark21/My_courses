# Алгоритм Евклида позволяет найти наибольший общий делитель (НОД) для двух чисел
#
# Давайте сперва освежим память и вспомним, что такое делитель. Делитель натурального числа a – это натуральное число b,
# на которое число a делится нацело.
#
# Например, делителем числа 6 являются числа: 1, 2, 3, 6.
#
# Простым числом называется такое натуральное число, которое имеет два делителя: единица и само это число.
# Например, простым числом будет являться число 5, так как у него только два делителя: 1 и 5.
# Также числа 7 и 13 будут являться простыми числами, а вот единица - нет. У единицы только один делитель,
# а должно быть два.
#
# Общий делитель - это число, которое может быть делителем каждого числа из указанного множества.
# Например, делители числа 10: 1, 2, 5, 10; а у числа 20: 1, 2, 4, 5, 10, 20.
# Общими делителями у 10 и 20 будут следующие числа: 1, 2, 5, 10.
#
# Наибольший общий делитель (НОД)
# Наибольший общий делитель (НОД) – это число,
# которое делит без остатка два числа и делится само без остатка на любой другой делитель данных двух чисел.
# Проще говоря, это самое большое число, на которое можно без остатка разделить два числа, для которых ищется НОД.
#
# В нашем примере с числами 10 и 20 наибольшим общим делителем будет число 10.
#
#
# Алгоритм Евклида: нахождение НОД вычитанием
# Алгоритм Евклида путём вычитания имеет следующий вид:
#
# Получаем числа a и b
# Пока a не равно b:
# Находим большее из них
# Вычитаем из большего числа меньшее.
# Выводим a или b (не имеет значение какое из чисел выводить, поскольку они равны)


# Алгоритм Евклида путём вычитания имеет следующий вид:
num_1, num_2 = map(int, input().split())
while num_1 != num_2:
    if num_1 > num_2:
        num_1 -= num_2
    else:
        num_2 -= num_1
print(f"Наибольший общий делитель(НОД) введённых чисел = {num_1}")


# Алгоритм Евклида через вычитание удобен и понятен, однако он имеет один большой недостаток: в ситуации,
# когда одно число намного больше другого процесс вычитания может занять слишком много времени.
#
# Например, если a = 100000000, b = 2, то алгоритм будет вычитать 2 из числа 100000000 до тех пор, пока не дойдёт до 2.
#
# В подобных случаях проще находить НОД при помощи деления.
#
# Алгоритм Евклида путём деления имеет следующий вид:
#
# Получаем числа a и b
# Пока b > 0:
# Добавим переменную c, в которую вносим остаток от деления a на b;
# В a кладём значение b
# В b кладём значение c
# Выводим a.
# Примечание: в данном примере мы изначально предположили, что a > b, но особого значения, поскольку если a < b,
# то программа сделает на один шаг больше, потратив его на перестановку значений в переменных.

# Алгоритм Евклида путём деления имеет следующий вид:

num_1, num_2 = map(int, input().split())

while num_2 > 0:
    num_3 = num_1 % num_2
    num_1 = num_2  # Короткий вариант записи num_1, num_2 = num_2, num_3
    num_2 = num_3  #

print(f"Наименьшее общее кратное (НОК) введённых чисел = {num_1}")


# Наименьшее общее кратное (НОК)
 # НОК = (a * b) / НОД

num_1, num_2 = map(int, input().split())
int_1, int_2 = num_1, num_2
while int_1 != int_2:
    if int_1 > int_2:
        int_1 -= int_2
    else:
        int_2 -= int_1
print(f"Наименьшее общее кратное (НОК) введённых чисел = ", int(num_1 * num_2) / int_1)
