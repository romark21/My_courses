# Проверьте, является ли двумерный массив симметричным относительно главной диагонали. Главная диагональ — та,
# которая идёт из левого верхнего угла двумерного массива в правый нижний.
#
# Входные данные
#
# Программа получает на вход число n<100, являющееся числом строк и столбцов в массиве.
# Далее во входном потоке идет n строк по n чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа должна выводить слово Yes для симметричного массива и слово No для несимметричного.
#
# Решение задачи Youtube Patreon Boosty
#
# Sample Input 1:
#
# 3
# 0 1 2
# 1 5 3
# 2 3 4
# Sample Output 1:
#
# Yes
# Sample Input 2:
#
# 3
# 0 0 0
# 0 0 0
# 1 0 0
# Sample Output 2:
#
# No
# Sample Input 3:
#
# 5
# 0 0 0 0 0
# 0 0 0 0 0
# 1 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# Sample Output 3:
#
# No
# Sample Input 4:
#
# 5
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# Sample Output 4:
#
# Yes


# 1 вариант
# n = int(input())
# matrix = [[*map(int, input().split())] for i in range(n)]
# count_yes = 0
# count_no = 0
#
# for i in range(len(matrix)):
#     for j in range(n):
#         if i == j:
#             continue
#         if matrix[i][j] != matrix[j][i]:
#             count_no += 1
#         else:
#             count_yes += 1
#
# print("yes" if count_no == 0 else "no")

# 2 вариант


n = int(input())
matrix = [[*map(int, input().split())] for i in range(n)]
result = "Yes"

for i in range(len(matrix)):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            result = "No"
            break

print(result)