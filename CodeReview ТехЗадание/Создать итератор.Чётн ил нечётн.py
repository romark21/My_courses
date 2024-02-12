"""
Сделал ка по первому заданию. Выводим только по одному параметру. В данном случае праграмма выводит по чётным индексам.
"""

class OddEven:

    def __init__(self, data):
        self.data = data
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.data):
            value = self.data[self.current]
            self.current += 2
            return f'"{value}" - Чётный индекс'
        else:
            raise StopIteration


my_data = ['one', 'two', 'three', 'car', 'phone', 7, 'python', '234']

it = OddEven(my_data)


for item in it:
    print(item)


# data = [*map(str, input('Введите элементы через пробел: ').split())]
# even_num = []
# odd_num = []
#
# for i in range(len(data)):
#     if i % 2 == 0:
#         even_num.append(data[i])
#     else:
#         odd_num.append(data[i])
#
# print(f'Элементы с чётным индексом: {even_num}')
# print(f'Элементы с нечётным индексом: {odd_num}')
#
# """
# --------------------------------------------------------------------------------------------------------------------
# """
#
# list = [*map(str, input('Введите элементы через пробел: ').split())]
# even_num = [list[i] for i in range(len(list)) if i % 2 == 0]
# odd_num = [list[i] for i in range(len(list)) if i % 2 != 0]
#
# print(f'Элементы с чётным индексом: {even_num}')
# print(f'Элементы с нечётным индексом: {odd_num}')






