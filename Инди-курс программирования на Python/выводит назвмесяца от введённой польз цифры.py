# Пользователь вводтит число, программа выводит названия месяца


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
count = 0
num = int(input())
for i in range(1, num):
    count += 1
print(months[count])
