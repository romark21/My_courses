def new_order() -> bool:
    answer = input(f"Будете делать новый заказ?; y/n:")
    if answer =='y':
        return False
    elif answer == 'n':
        return True


def get_order(ingredients: list) -> list:
    order = []
    for ingredient in ingredients:
        command = input(f"Добавить {ingredient}; y/n:")
        if command == 'y':
            order.append(ingredient)
    return order


def check_order(order: list) -> bool:
    if not order:
        print("Вы ничего не заказали! ")
        return new_order()
    for ingridient in order:
        print(ingridient)
    answer = input(f"Верный заказ? y/n: ")
    if answer == "y":
        print("Заказ принят! Ожидайте. ")
        return True
    elif answer == "n":
        return new_order()


def main() -> None:
    while True:
        ingredients = ['tomatoes', 'mushrooms', 'cheese', 'sausage', 'olives']
        order = get_order(ingredients)
        if check_order(order):
            exit()


main()