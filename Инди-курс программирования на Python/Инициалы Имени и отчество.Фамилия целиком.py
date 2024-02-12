# Ваша программа получает на вход строку, содержащую имя, отчество и фамилию человека
#
# Вам необходимо вывести фамилию и инициалы, как в примерах ниже
#
# Sample Input 1:
#
# Марина Денисовна Климова
# Sample Output 1:
#
# Климова М.Д.
# Sample Input 2:
#
# Марк Ильич Воробьев
# Sample Output 2:
#
# Воробьев М.И.

# 1ый вариант через списоки
name, mid_name, last_name = [str(i) for i in input().split()]
print(f"{last_name} {name[0]}.{mid_name[0]}.")

# 1ый вариант через строки
name, mid_name, last_name = input().split()
print(f"{last_name} {name[0]}.{mid_name[0]}.")