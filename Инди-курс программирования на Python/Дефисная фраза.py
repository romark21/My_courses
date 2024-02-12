# Вводится два слова через пробел. Ваша задача преобразовать данную фразу таким образом, чтобы все буквы стали заглавными
# и между буквами в каждом слове появились дефисы
#
# Решение Youtube Patreon Boosty
#
# Sample Input 1:
#
# Бросай курить
# Sample Output 1:
#
# Б-Р-О-С-А-Й К-У-Р-И-Т-Ь
# Sample Input 2:
#
# сИдИ дОмА
# Sample Output 2:
#
# С-И-Д-И Д-О-М-А

# 1ый вариант
a = [str(i) for i in input().upper().split()]
print(*a[0], sep='-', end=' ')
print(*a[1], sep='-')

# 2ой вариант
print(*['-'.join(i) for i in input().upper().split()])