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
    s_main = storona**2
    s_bok = 1/2 * apofema * storona * 4
    s_full = s_main + s_bok
    v = 1/3 * s_main * height
    print("Площадь полной поверхности пирамиды равна", "{0:.4f}".format(s_full))
    print("Объем пирамиды равен", "{0:.4f}".format(v))


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
    data = (boat_velocity, course_velocity, time_lake, time_river)
    for count in data:
        if count < 1 or count > 100:
            print("Ошибка! Одна из введенных величин не принадлежит промежутку [1;100]")
            return 0
    path = boat_velocity * time_lake + (boat_velocity - course_velocity) * time_river
    print("Путь равен", float("{0:.4f}".format(path)))


def task9():
    rubles = float(input("Введите сумму в рублях "))
    curse = float(input("Введите курс юаня "))
    comission = float(input("Введите коммисию"))
    yuan = rubles * curse * (1 - comission)
    print(f"{rubles} ₽ равно", float("{0:.3f}".format(yuan)), "¥")
