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
            return f' Number {num} squared is {num ** 2}'
        else:
            raise StopIteration


nums = Square()

for item in nums:
    print(item)