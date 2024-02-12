def operator_if_2() -> None:



    a = int(input("Введите число: "))
    b = int(input("Введите число: "))

    print(type(a))





    if a % 2 == 0:
        z = "Чётное число", a
        print(" ".join(map(str, z)))
    else:
        z = 'Не чётное число', a
        print(" ".join(map(str, z)))


    if b % 2 == 0:
        y = 'Чётное число', b
        print(" ".join(map(str, y)))

    else:
        y = 'Не чётное число', b
        print(" ".join(map(str, y)))

    if a > b:

        print(f'{" ".join(map(str, z))} больше, чем {" ".join(map(str, y))}')
    else:
        print(f'{" ".join(map(str, z))} меньше, чем {" ".join(map(str, y))}')


operator_if_2()