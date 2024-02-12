# 1ый вариант

tic_num = input("Введите 6-ти значный номер билета: ")
first_half_numb = int(tic_num[0]) + int(tic_num[1]) + int(tic_num[2])
second_half_numb = int(tic_num[3]) + int(tic_num[4]) + int(tic_num[5])


if len(tic_num) == 6:
    if first_half_numb == second_half_numb:
        print(f"Ваш билет с номером {tic_num} - Счастливый!!!")
    else:
        print(f"Ваш билет с номером {tic_num} - Обычный!!!")
else:
    print(f"Вы ввели не правильное количество цифр!!!")


# 2ой вариант спустя пару месяцев. Проходя курс Indy-программирование

t_num = list(map(int, input()))

if len(t_num) < 6:     # Добавляю "0" с помощью r.just до общего кол-во символов == 6
    t_num = [0] * (6 - len(t_num)) + t_num    # Добавляю "0" с помощью r.just до общего кол-во символов == 6
if sum(t_num[:3]) == sum(t_num[3:]):
    print("YES")
else:
    print("NO")

# 3ий вариант спустя пару месяцев. Проходя курс Indy-программирование. Допиленный.
t_num = list(map(int, input().rjust(6, '0')))  # Добавляю "0" с помощью r.just до общего кол-во символов == 6
if sum(t_num[:3]) == sum(t_num[3:]):
    print("YES")
else:
    print("NO")
