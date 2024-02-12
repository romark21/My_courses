def func_one() -> None:
    animals = {"Tiger", "Cat", "Dog", "Pig"}
    print(animals)
    print(type(animals))


#func_one()


def func_two() -> None:
    animals = {"Tiger", "Cat", "Tiger", "Dog", "Pig", "Dog"}
    print(animals)


#func_two()


def func_three() -> None:
    animals = {"Tiger", "Cat"}
    print(animals)
    animals.add("Dog")
    print(animals)


#func_three()



def func_four() -> None:
    animals = set(["Tiger", "Cat"])
    print(animals)
    animals.add("Dog")
    print(animals)



#func_four()




def func_five() -> None:
    animals = {"Tiger", "Cat"}
    print(animals)
    #animals.update("Dog")
    #print(animals)
    dog = {"Dog", "Cat"}
    #animals.update(dog)
    #print(animals)

    #result = animals.intersection(dog)
    result = animals.difference(dog)
    print(result)


#func_five()



def func_six() -> None:
    animals = {"Tiger", "Cat"}
    for i in animals:
        print(i)


#func_six()


def func_seven() -> None:
    animals = frozenset(["Tiger", "Cat"])
    print(animals)
    print(type(animals))



#func_seven()


### Решение задач по теме


def two_list() -> None:

    list_names = ['John', 'Bob', 'Mike', 'Anna']
    get_names = ['Bob', 'Elena', 'Anna', 'Victor']
    #new_list = list(set(list_names + get_names))
    #new_list = list(set(list_names) - set(get_names))
    #new_list = list(set(list_names) ^ set(get_names))
    new_list = list(set(list_names) & set(get_names))



    print(new_list)


if __name__ == '__main__':
    two_list()