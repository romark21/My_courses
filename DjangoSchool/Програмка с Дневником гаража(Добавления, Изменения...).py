def main():





    import pickle

    contacts = {"Петя": "BMW", "Лена": "AUDI", "Андрюха": "MAZDA"}
    while True:
        commands = input("1 - Добавить\n2 - Удалить\n3 - Просмотр\n4 - Загрузить данные\nВведите номер команды: ")
        print()
        if commands == "1":
            name = input("Введите имя: ")
            if contacts.get(name):
                print("Такое имя уже существует! ")
                continue
            car = input("Введите марку автомобиля:")
            contacts[name] = car
            answer = input("Сохранить изминения?")
            if answer.lower() == "Да":
                file = open("Дневник гаража.bin", "wb")
                pickle.dump(contacts, file)
                file.close()
            print("Изминения сохранены")
            if answer.lower() == "Нет":
                continue
        elif commands == "2":
            name = input("Введите имя: ")
            if contacts.get(name):
                contacts.pop(name)
                print(f"Водитель {name} удалён")
            else:
                print(f"Имя {name} не найдено! ")
        elif commands == "3":
            for name, car in enumerate(contacts.items(), start=1):
                print(f'{name} - {car}')
            print()
        elif commands == "4":
            file = open("Дневник гаража.bin", "rb")
            pickle.load(file)
            file.close()



    print(contacts)


if __name__ == '__main__':
    main()