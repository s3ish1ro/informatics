import math as m
def task1():
    x = int(input("Введите значение x "))
    y = int(input("Введите значение y "))
    z = int(input("Введите значение z "))
    a = (abs(x-1)**(1/3) + m.cos(y)) / (m.tan(y) + m.sinh(y))
    b = m.log(abs(z - 1)**(1/2) + abs(y)**(1/3) / (1 + z**2)**(1/2)) + m.sin(y) * m.sin(x)
    print(float("{0:.4f}".format(a)),float("{0:.4f}".format(b)))
