# Задан целочисленный двумерный массив, состоящий из N строк и M столбцов. Требуется вычислить сумму элементов
# в каждой строке и в каждом столбце.
#
# Программа получает на вход два натуральных числа N и M – количество строк и столбцов двумерного массива.
# В каждой из последующих N строк записаны M целых чисел – элементы массива.
# Все числа во входных данных не превышают 1000 по абсолютной величине.
#
# В первой строке вам необходимо вывести N чисел – суммы элементов массива для каждой строки в отдельности.
#
# Во второй строке в аналогичном формате выведите M чисел – суммы элементов для каждого столбца.
#
# Sample Input 1:
#
# 3 4
# 5 9 2 6
# 6 2 4 3
# 1 2 8 7
# Sample Output 1:
#
# 22 15 18
# 12 13 14 16
#
# Sample Input 2:
#
# 2 5
# 1 6 4 7 9
# 4 7 3 8 2
# Sample Output 2:
#
# 27 24
# 5 13 7 15 11

n, m = map(int, input().split())
matrix = [[*map(int, input().split())]for i in range(n)]
row_result = 0
overall_rows_results = []
column_result = 0
overall_columns_results = []

for row in range(len(matrix)):
    for column in range(m):
        row_result += matrix[row][column]
    overall_rows_results.append(row_result)
    row_result = 0

for column in range(m):
    for row in range(len(matrix)):
        column_result += matrix[row][column]
    overall_columns_results.append(column_result)
    column_result = 0

print(*overall_rows_results)
print(*overall_columns_results)