from functools import wraps
# import time
#
#
# def decoration_function(func):
#
#     @wraps(func)
#     def wrapper():
#         start_time = time.time()
#         print(func(1000))  #Для того чтобы декорируемая функция возвратила своё значение, нужно в этой строке написать: print(func())
#         # Чтобы функция принимала аргументы, нужно добавить аргумент. В нашем случае, аргументом является 1000.
#         finish_time = time.time() - start_time
#         return f'Время выполнения функции: {finish_time}'
#     return wrapper()
#
#
# @decoration_function
# def get_list(num):  # Чтобы функция принимала аргументы, нужно добавить параметр.
#     result = [i for i in range(num)]    # Подставить его в нужное нам место.
#     return result
#
#
# timer = get_list
# print(timer)


def decoration_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):



        return func(*args, **kwargs)
    return wrapper()

@decoration_function
def my_func(x, y, z):
    return (x + y) * z

print(my_func(3, 4, 6))
