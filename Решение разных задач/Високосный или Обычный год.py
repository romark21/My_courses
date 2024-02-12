def visokos_god():

    a = int(input("Введите год (с 1900 по 3000): "))
    b = a % 4 == 0 and a % 100 != 0 or a % 400 == 0

    if 1900 <= a <= 3000:
        if b is True:
            print(f"Введённый вами {a} год, является - Високосный!")
        else:
            print(f"Введённый вами {a} год, является - Обычный!")


visokos_god()
