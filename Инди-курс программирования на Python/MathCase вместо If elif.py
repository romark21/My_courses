"""
------------------------------------------------------------------------------------------------------------------

# Давайте попробуем потренироваться в операторе match-case
#
# Чуть ранее студенты технических специальностей университета учились 5 лет (специалитет) и затем им вручался аттестат.
# Ваша программа программа будет получать на вход целое число - номер курса,
# и в зависимости от номера выводить следующий текст
#
# если ввели 1, выведите сообщение Совсем еще зеленый студентик
# если ввели 2, выведите сообщение Джун-студент
# если ввели 3, выведите сообщение Мидл-студент
# если ввели 4, выведите сообщение Сеньор-студент
# если ввели 5, выведите сообщение Босс качалки
# при вводе остальных значений, выведите текст Неизвестный курс
# Используйте при решении оператор match-case


num = int(input())
match num:
    case 1:
        print("Совсем еще зеленый студентик")
    case 2:
        print("Джун-студент")
    case 3:
        print("Мидл-студент")
    case 4:
        print("Сеньор-студент")
    case 5:
        print("Босс качалки")
    case _:
        print("Неизвестный курс")




# Часто можно услышать такой вопрос. Давайте это запрограммируем.
#
# Программа получает на вход номер месяца - натуральное число N (1 ≤ N ≤ 12) и в зависимости от его значения
# выводит количество дней в месяце. Будем считать, что год невисокосный. При решении конечно же
# используйте оператор match-case
#
#  Cколько дней в каком месяце
#
# Январь - 31 день
# Февраль - 28 дней
# Март - 31 день
# Апрель - 30 дней
# Май - 31 день
# Июнь - 30 дней
# Июль - 31 день
# Август - 31 день
# Сентябрь - 30 дней
# Октябрь - 31 день
# Ноябрь - 30 дней
# Декабрь - 31 день
# Для проверки данной задачи уже выставлена версия python3.10. Вам переключать ничего не нужно
#
# Sample Input 1:
#
# 1
# Sample Output 1:
#
# 31
# Sample Input 2:
#
# 2
# Sample Output 2:
#
# 28
# Sample Input 3:
#
# 6
# Sample Output 3:
#
# 30

num_of_month = int(input())
match num_of_month:
    case 1 | 3 | 5 | 7 | 8 | 10| 12:
        print(31)
    case 4 | 6 | 9 | 11:
        print(30)
    case 2:
        print(28)


# Программа ваша получает на вход строку - название знака зодиака и затем сообщает к какому типу относится введенный знак.
# Логика определения следующая:
#
# если введут любое из значений Овен, Лев, Стрелец, то программа выводит текст Огненный
# если введут любое из значений Телец, Дева, Козерог, то программа выводит текст Земной
# если введут любое из значений Близнецы, Весы, Водолей, то программа выводит текст Воздушный
# если введут любое из значений Рак, Скорпион, Рыбы, то программа выводит текст Водный
# Sample Input 1:
#
# Водолей
# Sample Output 1:
#
# Воздушный
# Sample Input 2:
#
# Лев
# Sample Output 2:
#
# Огненный
# Sample Input 3:
#
# Скорпион
# Sample Output 3:
#
# Водный

zodiac_sign = input()
match zodiac_sign:
    case "Овен" | "Лев" | "Стрелец":
        print("Огненный")
    case "Телец" | "Дева" | "Козерог":
        print("Земной")
    case "Близнецы" | "Весы" | "Водолей":
        print("Воздушный")
    case "Рак" | "Скорпион" | "Рыбы":
        print("Водный")

------------------------------------------------------------------------------------------------------------------
"""
SELECT title, name_author, name_genre, price, amount
FROM book
     INNER JOIN author
     ON book.author_id = author.author_id
     INNER JOIN genre
     ON genre.genre_id = book.genre_id
GROUP BY title, name_author, name_genre, price, amount
HAVING



SELECT title, name_author, name_genre, price, amount
FROM book INNER JOIN author
     ON book.author_id = author.author_id
     INNER JOIN genre
     ON genre.genre_id = book.genre_id
GROUP BY title, name_author, name_genre, price, amount
WHERE genre_id = (SELECT genre_sum_amount.genre_id
                  FROM