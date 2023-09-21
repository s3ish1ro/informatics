import math as m
def task1():
    x = int(input("Введите значение x "))
    y = int(input("Введите значение y "))
    z = int(input("Введите значение z "))
    a = (abs(x-1)**(1/3) + m.cos(y)) / (m.tan(y) + m.sinh(y))
    b = m.log(abs(z - 1)**(1/2) + abs(y)**(1/3) / (1 + z**2)**(1/2)) + m.sin(y) * m.sin(x)
    print(float("{0:.4f}".format(a)),float("{0:.4f}".format(b)))
def task2():
    x = int(input("Введите значение x"))
    a = 2
    b = 1
    c = -1
    print(float("{0:.4f}".format(((x**2 + a * x/b) + c * x**2)**(1/2))))


def task3():
    x = int(input("Введите значение x"))
    print(float("{0:.4f}".format(m.tan(x)**2 * abs(m.log(x**2)))))

def task4():
    print("введите координаты первой вершины")
    vershina1 = (int(input()), int(input()))
    print("введите коориданты второй вершины")
    vershina2 = (int(input()), int(input()))
    print("введите координаты третьей вершины")
    vershina3 = (int(input()), int(input()))


    storona1 = ((vershina2[0] - vershina1[0])**2 + (vershina2[1] - vershina1[1])**2)**0.5
    storona2 = ((vershina3[0] - vershina1[0])**2 + (vershina3[1] - vershina1[1])**2)**0.5
    diagonale1 = ((vershina3[0] - vershina2[0])**2 + (vershina3[1] - vershina2[1])**2)**0.5

    perimetr = storona1 * 4
        print("Заданная фигура не является ромбом")
    else:
        print(float("{0:.4f}".format(ploshad)),float("{0:.4f}".format(perimetr)))

task4()