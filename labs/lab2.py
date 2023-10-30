import matplotlib.pyplot as plt
import numpy as np
import math as m


def task1():
    def func1(x):
        if (x % 10) % 2 == 0:
            return True
        else:
            return False

    def func2(x, y):
        if x > y:
            return True
        else:
            return False

    x = int(input("Введите число"))
    y = int(input("Введите число для сравнения"))
    if func1(x):
        print("Число оканчивается на чётную цифру")
    else:
        print("Число оканчивается на нечётную цифру")
    if func2(x, y):
        print(f'{x} больше чем {y}')
    else:
        print(f'{x} меньше чем {y}')


def task2():
    def f(x):
        if x >= m.pi:
            return m.cos(x) + m.sin(x)
        else:
            return m.cos(x) - m.sin(x)

    d_y = (int(input("введите область определения функции \n")), int(input()))
    vector_x = [x for x in range(d_y[0], d_y[1] + 1)]
    vector_y = [f(x) for x in range(d_y[0], d_y[1] + 1)]
    plt.plot(vector_x, vector_y)
    plt.grid()
    plt.show()


def task3():
    number = int(input("Введите число в 10-чной СС "))
    base = int(input("Введите основание новой СС "))

    def number_in_new_numeral_system(number, base):
        count = 0
        n = 0
        while number != 0:
            count += (number % base) * 10**n
            number //= base
            n += 1
        print(count)
    number_in_new_numeral_system(number, base)


def task4():
    theta = np.linspace(np.pi / 2, 3 * np.pi / 2, 150)

    radius = 2

    a1 = radius * np.cos(theta) - 1
    b1 = radius * np.sin(theta) + 3
    x1 = [-1, 1, 0, -1]
    y1 = [5, 2, -1, 1]
    axes = plt.subplot()
    axes.plot(a1, b1, color='black')
    axes.plot(x1, y1, color='black')
    axes.set_aspect(1)

    theta2 = np.linspace(np.pi, 2 * np.pi, 150)
    radius = 2

    a2 = radius * np.cos(theta2) + 4
    b2 = radius * np.sin(theta2) - 1
    x2 = [2, 3, 2, 7, 6]
    y2 = [-1, 0, 1, 0, -1]
    axes.plot(x2, y2, color='black')
    axes.plot(a2, b2, color='black')
    plt.grid()
    plt.title('Task 4')

    def check1(x, y):
        """
        функция проверяет попадает ли точка в левую заданную область с помощью уравнений,
        так же для удобства область поделена на 2 части(полуокружность и многоугольник)
        """
        r = 2
        if (x + 1) ** 2 + (y - 3) ** 2 <= r ** 2 and x < -1:
            return True
        elif x >= -1 and -1.5 * (x - 1) + 2 >= y >= 3 * x - 1 and y >= -2 * x - 1:
            return True
        else:
            return False

    def check2(x, y):
        """
        функция проверяет попадает ли точка в правую заданную область с помощью уравнений,
        так же для удобства область поделена на 3 части(полуокружность, параллелограмм и треугольник)
        """
        r = 2
        if y < -1 and (x - 4) ** 2 + (y + 1) ** 2 == r ** 2:
            return True
        # упрощенное условие -1 <= y <= 0 and y <= x - 3 and y >= x - 7
        elif -1 <= y <= x - 3 and x - 7 <= y <= 0:
            return True
        # упрощенное условие y >= 0 and y >= -x + 3 and y <= -0.2 * x + 1.4
        elif 0 <= y <= -0.2 * x + 1.4 and y >= -x + 3:
            return True
        else:
            return False

    x = float(input("введите координату x точки "))
    y = float(input("введите координату y точки "))
    if check1(x, y):
        print("Точка принадлежит первой фигуре")
    elif check2(x, y):
        print("Точка принадлежит второй фигуре")
    else:
        print("Точка не принадлежит ни одной из фигур")
    axes.scatter(x, y)
    plt.show()


def task5():
    ans = [int(input("Введите число ")) for x in range(3)]
    print(f"Максимальное значение равно {max(ans)}",f"Минимальное значение равно {min(ans)}")
