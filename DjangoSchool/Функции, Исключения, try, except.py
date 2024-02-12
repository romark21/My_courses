def func():
    pass

# def my_name(name):


def calc(a, b): #Функция calc складывает числа.
    c = a + b
    return c

result = calc(1, 3)
print(result)


def calc(a, b=5): # Необязательный аргумент.Если не будет указана в условии ниже цифра для "b", тогда присвоиться 5ка.
    c = a + b
    return c

result = calc(1)
print(result)

print("------------------")

def my_func(*args): # *args именно с одной "*" - Позиционный необязательный аргумент
    print(args)
    print(type(args))

my_func(1, 2, 3, "Hi", 4)

my_test_list = [1, 2, 3, "Hi", 4] #Передаём список в функцию. Но он отображается как картеж одним элементом.
my_func(my_test_list)

my_test_list = [1, 2, 3, "Hi", 4]
my_func(*my_test_list) # Поставить * чтобы развернуть список

print("-------------------")

def my_func_2(**kwargs): # Необязательные именованные (даём имя) аргументы.
    print(kwargs)
    print(type(kwargs))

my_func_2(key=1, word="Hi", number=4)

my_test_dict = {"key": 1, "word": "Hi", "number": 4} #Используя словаря нужно поставить ** , иначе будет ошибка
my_func_2(**my_test_dict)


