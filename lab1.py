import math as m
def task1():
    x = float(input("Введите значение x "))
    y = float(input("Введите значение y "))
    z = float(input("Введите значение z "))
    a = (abs(x-1)**(1/3) + m.cos(y)) / (m.tan(y) + m.sinh(y))
    b = m.log(abs(z - 1)**(1/2) + abs(y)**(1/3) / (1 + z**2)**(1/2)) + m.sin(y) * m.sin(x)
    print(float("{0:.4f}".format(a)),float("{0:.4f}".format(b)))
def task2():
    x = float(input("Введите значение x"))
    a = 2
    b = 1
    c = -1
    print(float("{0:.4f}".format(((x**2 + a * x/b) + c * x**2)**(1/2))))


def task3():
    x = float(input("Введите значение x"))
    print(float("{0:.4f}".format(m.tan(x)**2 * abs(m.log(x**2)))))

def task4():
    print("введите координаты первой вершины")
    vershina1 = (float(input()), float(input()))
    print("введите коориданты второй вершины")
    vershina2 = (float(input()), float(input()))
    print("введите координаты третьей вершины")
    vershina3 = (float(input()), float(input()))


    storona1 = ((vershina2[0] - vershina1[0])**2 + (vershina2[1] - vershina1[1])**2)**0.5
    storona2 = ((vershina3[0] - vershina1[0])**2 + (vershina3[1] - vershina1[1])**2)**0.5
    diagonale1 = ((vershina3[0] - vershina2[0])**2 + (vershina3[1] - vershina2[1])**2)**0.5
    diagonale2 = (storona1**2 + 1/2 * diagonale1**2)**0.5
    perimetr = storona1 * 4
    ploshad = 1/2 * diagonale1 * diagonale2
    if storona1 != storona2:
        print("Заданная фигура не является ромбом")
    else:
        print(float("{0:.4f}".format(ploshad)),float("{0:.4f}".format(perimetr)))

def task5():
    G = 6.67 * 10**(-11)
    mass1 = float(input("введите массу первого тела"))
    mass2 = float(input("введите массу второго тела"))
    distance = float(input("введите расстояние между телами"))
    F = G * (mass1 * mass2) / distance**2
    print(F)

def task6():
    storona = float(input("введите длину стороны основания"))
    height = float(input("введите высоту пирамиды"))
    apofema = ((storona / 2)**2 + height**2)**0.5
    S_main = storona**2
    S_bok = 1/2 * apofema * storona * 4
    S_full = S_main + S_bok
    print("{0:.4f}".format(S_full))

def task7():
    x1 = float(input("введите координату первой точки"))
    x2 = float(input("введите координату второй точки"))
    print("{0:.4f}".format(abs(x2 - x1)))

