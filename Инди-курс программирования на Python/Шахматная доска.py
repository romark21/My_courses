# Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит сообщение о том,
# являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются английскими строчными буквами.
#
# Программа должна выводить YES, когда клетки одного цвета, NO - разного. Гарантируется,
# что значение колонок это латинские буквы abcdefgh, а строки это символы цифр от 1-8

coord_1 = list(str(i) for i in input())
coord_2 = list(str(i) for i in input())
white = 0
black = 0


if coord_1[0] in ['a', 'c', 'e', 'g'] and int(coord_1[1]) % 2 == 0\
        or coord_1[0] in ['b', 'd', 'f', 'h'] and int(coord_1[1]) % 2 != 0:
    white += 1
else:
    black += 1

if coord_2[0] in ['a', 'c', 'e', 'g'] and int(coord_2[1]) % 2 == 0\
        or coord_2[0] in ['b', 'd', 'f', 'h'] and int(coord_2[1]) % 2 != 0:
    white += 1
else:
    black += 1


print("YES" if white != black else "NO")