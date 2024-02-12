array = [1, 5, 0, -5, 2.5]
for n in array:
    print(n)

print("----------------")

str = "Phyton"
print(str[0])

for s in str:
    print(s)

for s in str:
    if s == "Y":
        break
else:
    print("Символа Y в строке", str, "нет")

print("========================")

# Генераторы списков
# Первый генератор

array = list(range(2, 15))
print(array[0])
for n in array:
    print(n)

print("========================")

array = [i for i in range(1, 10)]
print(array)
array = [i * 2 for i in range(1, 10)]
print(array)
array = [i for i in range(1, 10) if i % 2]
print(array)