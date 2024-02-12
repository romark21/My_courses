# Переберает числа, если хоть одно число чётное, выводит "NO"
list = [34, 56, 78, 126, 43, 78]

while len(list) > 0:
    last_digit = list.pop()
    if last_digit % 2 == 0:
        print("No")
        break  # Если срабатывает Break, то всё что ниже в блоке не выполняется
    else:
        ("Yes")