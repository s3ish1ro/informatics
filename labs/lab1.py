import math as m


def task1():
    x = float(input("Введите значение x "))
    y = float(input("Введите значение y "))
    z = float(input("Введите значение z "))
    a = (abs(x-1)**(1/3) + m.cos(y)) / (m.tan(y) + m.sinh(y))
    b = m.log(abs(z - 1)**(1/2) + abs(y)**(1/3) / (1 + z**2)**(1/2)) + m.sin(y) * m.sin(x)
    print("a =", float("{0:.4f}".format(a)))
    print("b =", float("{0:.4f}".format(b)))


def task2():
    x = float(input("Введите значение x "))
    a = 2
    b = 1
    c = -1
    function = ((x**2 + a * x/b) + c * x**2)**0.5
    print("значение функции равно", float("{0:.4f}".format(function)))


def task3():
    x = float(input("Введите значение x "))
    function = m.tan(x)**2 * abs(m.log(x**2))
    print("значение функции равно", float("{0:.4f}".format(function)))


def task4():
    print("введите координаты первой вершины ")
    vershina1 = (float(input()), float(input()))
    print("введите коориданты второй вершины ")
    vershina2 = (float(input()), float(input()))
    print("введите координаты третьей вершины ")
    vershina3 = (float(input()), float(input()))
    EPS = 10e-3

    storona1 = ((vershina2[0] - vershina1[0])**2 + (vershina2[1] - vershina1[1])**2)**0.5
    storona2 = ((vershina3[0] - vershina1[0])**2 + (vershina3[1] - vershina1[1])**2)**0.5
    diagonale1 = ((vershina3[0] - vershina2[0])**2 + (vershina3[1] - vershina2[1])**2)**0.5
    diagonale2 = (storona1**2 + 1/2 * diagonale1**2)**0.5
    perimetr = storona1 * 4
    ploshad = 1/2 * diagonale1 * diagonale2
    if abs(storona1 - storona2) >= EPS:
        print("Заданная фигура не является ромбом")
    else:
        print("Площадь равна", float("{0:.4f}".format(ploshad)))
        print("Периметр равен", float("{0:.4f}".format(perimetr)))


def task5():
    G = 6.67 * 10**(-11)
    mass1 = float(input("введите массу первого тела "))
    mass2 = float(input("введите массу второго тела "))
    distance = float(input("введите расстояние между телами "))
    F = G * (mass1 * mass2) / distance**2
    print("Сила притяжения между телами равна", F, sep=" ")


def task6():
    storona = float(input("введите длину стороны основания "))
    height = float(input("введите высоту пирамиды "))
    apofema = ((storona / 2)**2 + height**2)**0.5
    S_main = storona**2
    S_bok = 1/2 * apofema * storona * 4
    S_full = S_main + S_bok
    print("Площадь полной поверхности пирамиды равна", "{0:.4f}".format(S_full))


def task7():
    x1 = float(input("введите координату первой точки "))
    x2 = float(input("введите координату второй точки "))
    print("Расстояние между телами равно ", "{0:.4f}".format(abs(x2 - x1)))


def task8():
    boat_velocity = float(input("Введите скорость лодки "))
    course_velocity = float(input("Введите скорость течения "))
    if boat_velocity <= course_velocity:
        print("Ошибка! Скорость течения больше скорости лодки")
    time_river = float(input("Введите время движения против течения реки "))
    time_lake = float(input("Введите время движения по озеру"))
    if boat_velocity < 1:
        print("Ошибка! Скорость лодки меньше 1")
    elif course_velocity < 1:
        print("Ошибка! Скорость течения меньше 1")
    elif time_river < 1:
        print("Ошибка! Время движения против течения реки меньше 1")
    elif time_lake < 1:
        print("Ошибка! Время движения по озеру меньше одного ")
    elif boat_velocity > 100 or course_velocity > 100 or time_lake > 100 or time_river > 100:
        print("Ошибка! Одна из введённых величин больше 100")

    path = boat_velocity * time_lake + (boat_velocity - course_velocity) * time_river
    if 1 < boat_velocity < 100 and 1 < course_velocity < 100 \
            and 1 < time_river < 100 and 1 < time_lake < 100:
        print("Путь равен", float("{0:.4f}".format(path)))


def task9():
    rubles = float(input("Введите сумму в рублях "))
    commision = float(input("Введите курс Юаня "))
    yuan = rubles * commision
    print(f"{rubles} ₽ равно", float("{0:.3f}".format(yuan)), "¥")
