class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Animal):
    def mjau(self):
        print("Mjau-mjau")

class Dog(Animal):
    def __init__(self, name, last_name, age):
        super().__init__(name, age)
        self.last_name = last_name
    def gaf(self):
        print("Gaf-gaf")



cat = Cat("Bob", 2)
cat.mjau()
print(cat.name, cat.age)

dog = Dog("Polkan", "Fridrih", 7)
dog.gaf()
print(dog.name, dog.last_name, dog.age)


