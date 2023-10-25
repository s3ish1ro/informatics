import matplotlib.pyplot as plt
import numpy as np
import math as m


def task1():
    def func1(x):
        if (x % 10) % 2 == 0:
            return True
        else:
            return False


    def func2(x,y):
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
    if func2(x , y):
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
    vector_x = [x for x in range(d_y[0],d_y[1] + 1)]
    vector_y = [f(x) for x in range(d_y[0],d_y[1] + 1)]
    plt.plot(vector_x, vector_y)
    plt.grid()
    plt.show()


def task3():
    number = int(input("Введите число в 10-чной СС "))
    base = int(input("Введите основание новой СС "))
    def number_in_new_numeral_system(number,base):
        count = 0
        n = 0
        while number != 0:
            count += (number % base) * 10**n
            number //= base
            n += 1
        print(count)
    number_in_new_numeral_system(number,base)


def task5():
    list = (float(input("Введите")))
