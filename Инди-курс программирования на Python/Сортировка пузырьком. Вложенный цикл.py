# Все просто, вам поступает число n - количество элементов в списке, и затем сам список.
#
# Ваша задача отсортировать список по возрастанию при помощи пузырьковой сортировки,
# в случае если элементы соседние совпадают менять их ненужно.
#
# В качестве ответа нужно вывести отсортированный список и какое количество раз пришлось переставлять
# элементы в процессе сортировки
#
# Sample Input 1:
#
# 7
# 8 5 3 1 4 7 9
# Sample Output 1:
#
# 1 3 4 5 7 8 9
# 9
# Sample Input 2:
#
# 3
# 9 8 -4
# Sample Output 2:
#
# -4 8 9
# 3
# Sample Input 3:
#
# 7
# 7 13 -18 10 -14 4 -6
# Sample Output 3:
#
# -18 -14 -6 4 7 10 13
# 13

num_of_items = int(input())
num_list = [*map(int, input().split())]
count = 0

for i in range(len(num_list) - 1):
    for j in range(len(num_list) - 1 - i):
        if num_list[j] > num_list[j + 1]:
            num_list.insert(j, num_list.pop(j + 1))
            count += 1
print(count)