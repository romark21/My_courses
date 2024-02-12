# class OddEven:
#
#     def __init__(self, data):
#         self.data = data
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < len(self.data):
#             value = self.data[self.current]
#             self.current += 1
#             if self.current % 2 == 0:
#                 return f'"{value}" - Чётный индекс'
#             else:
#                 return f'"{value}" - Нечётный индекс'
#         else:
#             raise StopIteration
#
#
# my_data = ['one', 'two', 'three', 'car', 'phone', 7, 'python', '234']
#
# it = OddEven(my_data)
#
# for count, item in enumerate(it, 1):
#     print(count, item)
import random


class Square:

    def __init__(self):
        self.start = 0
        self.finish = random.randint(1, 20)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.finish:
            num = self.start
            self.start += 1
            return f' Число {num} в квадрате, равна {num ** 2}'
        else:
            raise StopIteration


nums = Square()

for item in nums:
    print(item)
