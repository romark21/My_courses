def main():

    name = "Michael".upper()
    n = 0
    for i in name:
        print(i)
        n += 1 #упращённая запись n = n + 1
        print(n)

    print("----------")
 # Или таким способом
    name = "Michael".upper()
    for n, i in enumerate(name):
        print(i)
        print(n)


    print("----------")
    for name in ["Tom", "John", "Bob"]:
        print(name)


    print("----------")
    list_number = [1, 2, 3, 4, 5]
    #print(list_number)

    #list_number = [1, "Hi", [3, 4], 5]
    #print(list_number)

    #list_number[3] = "Test"
    list_number.append("Test")
    print(list_number)

    print("----------")

    names = ["Иван", "Мария", "Петр", "Андрей", "Лена"]
    friend_name = input("Введите имя для проверки: ")
    for name in names:
        if friend_name == name:
            print(f"Имя {friend_name} найдено")

    print("----------")

    list_name = ["Иван", "Мария", "Петр", "Андрей", "Лена"]
    name = input("Введите имя для проверки: ")
    name = name.title()
    if name.title() in list_name:
            print(f"Имя {name} найдено")
    else:
        print(f"Имя {name} не найдено")

    print("----------")

# 1 вариант (длинный)
    play_list = ["Sound1", "Sound2","Sound3","Sound4", "Sound5"]
    print(play_list)

    s1 = play_list[1]
    s2 = play_list[3]
    play_list[1] = s2
    play_list[3] = s1
    print(play_list)

# 2 вариант (короче)

    s1 = play_list[1]
    s2 = play_list[3]
    play_list[1], play_list[3] = s1, s2
    print(play_list)

# 3 вариант    play_list[1], play_list[3] = play_list[3], play_list[1]
#              print(play_list)




















if __name__ == "__main__":
        main()