triangle_cirkle_ractangle = input("Введите тип фигуры комнаты и соответствующие параметры (треугольник, прямоугольник или круг): ")

if triangle_cirkle_ractangle == "треугольник":
    a = float(input("Введите длину стороны треугольника 'a': "))
    b = float(input("Введите длину стороны треугольника 'b': "))
    c = float(input("Введите длину стороны треугольника 'c': "))
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    s **= 0.5
    print(f"Площадь треугольника ровна: {s}")
elif triangle_cirkle_ractangle == "прямоугольник":
    a = float(input("Введите длину: "))
    b = float(input("Введите ширину: "))
    s = a * b
    print(f"Площадь прямоугольника ровна: {s}")
elif triangle_cirkle_ractangle == "круг":
    pi = 3.14
    r = float(input("Введите радиус круга: "))
    s = pi * r ** 2
    print(f"Площадь круга ровна: {s}")