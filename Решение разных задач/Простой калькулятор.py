def simple_calculator():


    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    x = input("Введите знак '+, -, /, *': ")


    if (x == "mod" or x == "div" or x == "/") and (b == 0):
        print("Деление на 0!")
    else:
        if x == "+":
            print(a + b)
        elif x == "-":
            print(a - b)
        elif x == "/":
            print(a / b)
        elif x == "*":
            print(a * b)
        elif x == "mod":
            print(a % b)
        elif x == "pow":
            print(a ** b)
        elif x == "div":
            print(a // b)


simple_calculator()
