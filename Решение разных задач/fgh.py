def practik() ->None:
    s = "Hello World"
    num = 0
    for i in s:
        num += 1
        print(f"{num}. {i.upper()}")

#practik()


def practik_2() ->None:
    s = "Hello1 World\n 234"
    print(s.strip())

#practik_2()



def practik_3() ->None:

    gendere = {
        'm': 'Дорогой',
        'f': 'Дорогая'
    }
    People_list = [
        ["Валерий Иванович", "Смирнов", 456.08, 'm'],
        ["Анна Ивановна", "Пушкова", 3456.87, 'f'],
        ["Леонид Гайдарович", "Плишня", 2348.09, 'm'],
        ["Галина Сергеевна", "Страхажоповна", 5675467.98, 'f'],

]
    for name, last_name, balance, g in People_list:

        print(f"{gendere[g]} {name}...блин...фамилию забыл...ааа... {last_name}, баланс Вашего счёта: {balance} EUR.")



#practik_3()




def spiski() -> None:

    l = []
    lis = [1, 56, 'x', 34, 2.34, ['S', 't', 'r', 'k', 'a']]
    print(lis)

    a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
    print(a)

    l.append(34)
    l.append(34)
    b = [24, 67]
    l.extend(b)
    l.insert(1, 47)
    l.remove(34)
    l.pop (0)
    print(l.count(34))
    l.sort()

    print(l)

#spiski()

def spiski_egoroff() -> None:

    a = [34, 56, 76,45]
    b = ['Waflja', ]
    a.append('Hello')
    a.append(45)
    a.extend(b)
    a.remove(76)
    b.insert(1, 456)
    a.extend(b)

    print(a)




#spiski_egoroff()


def operator_if() -> None:
    a = 56
    if 59 > a:
        print("yes")
        if 57 == a:
            print("Fuck")

    else:
        print("NO")
    print(4)
    print(7)
    print(56)

#operator_if()

def operator_if_2() -> None:



    a = int(input("Введите число: "))
    b = int(input("Введите число: "))

    print(type(a))





    if a % 2 == 0:
        z = ["Чётное число", a]
        print(" ".join(map(str, z)))
    else:
        z = ['Не чётное число', a]
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
        print(f'{" ".join(map(str, z))} больше, чем  {" ".join(map(str, z))}')


#operator_if_2()

def operator_if_3() -> None:
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))

    if a > b and a % 2 == 0:
        print(f'Число {a} больше, чем число {b}')
    else:
        print(f'Число {b} больше, чем число {a}')





#operator_if_3()





def turttle() -> None:
    import turtle
    turtle.shape("turtle")
    turtle.shapesize(2)
    turtle.color('blue', 'yellow')



    def zvezda():
        for step in range(6):
            turtle.begin_fill()
            #for i in range(8):
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(100)
            turtle.end_fill()

            turtle.forward(50)
            turtle.right(60)


    zvezda()
    turtle.done()
turttle()



