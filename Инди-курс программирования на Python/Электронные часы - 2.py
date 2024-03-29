"""Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов в диапазоне
от 0 до 23, потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд.
Количество минут и секунд при необходимости дополняются до двузначного числа нулями.

Программа получает на вход число n - количество секунд, которое прошло с начала суток.

Выведите показания часов, соблюдая формат."""

n = int(input())

hour = n // 3600
minute = n // 60 % 60
seconds = n - (hour * 3600) - minute * 60
print(hour, str(minute).zfill(2), str(seconds).zfill(2), sep=':')