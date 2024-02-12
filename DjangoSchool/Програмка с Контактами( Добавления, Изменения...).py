def main():
    contacts = {"Петя": 111222, "Лена": 443322, "Андрюха": 564235}
    while True:
        command = input("1 - Добавить\n2 - Удалить\n3 - Просмотреть\n4 - Изменить номер контакта\nВведите команду: ")
        if command == '1':
            name = input("Введите имя: ")
            if contacts.get(name):
                print("Такое имя уже существует")
                continue
            tel = int(input("Введите номер телефона: "))
            contacts[name] = tel
        elif command == '2':
            name = input("Введите имя: ")
            if contacts.get(name):
                contacts.pop(name)
                print(f"Контакт {name} удалён")
            else:
                print(f"Имя {name} не найдено")
        elif command == '3':
            for name, phone in contacts.items():
                print(f"{name} - {phone}")
        elif command == '4':
            name = input("Введите имя контакта: ")
            if contacts.get(name):
                tel = int(input("Введите номер телефона: "))
                contacts.update([(name, tel)])
            else:
                print(f"Контакт {name} не найден")


if __name__ == '__main__':
    main()