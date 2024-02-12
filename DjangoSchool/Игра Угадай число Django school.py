import random


def main():
    while True:
        random_number = random.randint(0, 10)
        user_number = int(input("Введите число от 0 до 10: "))


        if user_number == random_number:
            print("Да. Вы угадали. Поздравляю!")
        else:
            print("Нет. Вы не угадали.")


        answer = input("Играем ещё раз? ")

        if answer == "Нет":
            break
        elif answer == "Да":
            continue


if __name__ == "__main__":
    main()