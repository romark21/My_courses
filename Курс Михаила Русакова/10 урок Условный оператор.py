print("Введите 0, 1 или 2")
a = input()
if a == "0":
    print("Вы ввели ноль")
elif a == "1":
    print("Вы ввели один")
elif a == "2":
    print("Вы ввели два")
else:
    print("Не корректный ввод")

cond = a == "0" or a == "1" or a == "2"
if cond:
    x = 0
else:
    x = 3

print("x =", x)