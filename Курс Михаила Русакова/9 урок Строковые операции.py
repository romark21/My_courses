mystr1 = "abc"
mystr2 = "xyz"
print("Конкатенация строк mystr1 и mystr2 =", mystr1 + mystr2) #Функция сложение строк

mystr1 = '''Длинная строка
на несколько
строк
'''
print(mystr1)
#Получение данных от пользователя

print("Сложение строк")
number1 = input("Введите первое число:")
print("Вы ввели: ", number1)
number2 = input("Введите второе число:")
print("Вы ввели: ", number2)
print("Результат:", number1 + number2)

print("_________")

#Для возможности сложения целых чисел.
print("Сложение целых чисел")
number1 = int(input("Введите первое число:"))
print("Вы ввели: ", number1)
number2 = int(input("Введите второе число:"))
print("Вы ввели: ", number2)
print("Результат:", number1 + number2)

print("_________")

print("Введите первое число")
number1 = input()
print("Введите второе число")
number2 = input()
print("Результат: ")
print(int(number1) + int(number2))

print("_________")

#Для возможности сложения десятичных чисел.
print("Сложение десятичных чисел")

print("Введите число: ")
number1 = input()
print("Введите число: ")
number2 = input()
print("Результат:", float(number1) + float(number2))