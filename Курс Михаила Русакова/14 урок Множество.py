import random

myset = set("Phytonn")
print(myset)

myset = {"1", 2, 3, 1,}
print(myset)



arr = [int(random.random() * 10)for i in range(0, 10)]
print(arr)
arr = list(set(arr))
print(arr)