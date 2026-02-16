import numpy as np

def f(x):
    return np.tan(x)**2

def df(x):
    return 2 * np.tan(x)/np.cos(x)**2

def d2f(x):
    return (2 + 4 * np.sin(x)**2)/np.cos(x)**4

a = 0.1
b = 1.5
n = 100
nc = []
g = []
for _ in range(4):
    h = (b - a)/n
    n_left = g_left = 0
    n_mid = g_mid = 0
    n_right = g_right = 0
    n_d2 = g_d2 = 0
    y_left = []
    y_right = []
    y_mid = []
    y_true = []
    y_d2 = []
    y_d2true = []
    for i in range(1, n):
        x_i = h * i
        y_left.append((f(x_i) - f(x_i - h))/h)
        y_right.append((f(x_i + h) - f(x_i))/h)
        y_mid.append((f(x_i + h) - f(x_i - h))/(2 * h))
        y_true.append(df(x_i))

        y_d2.append((f(x_i - h) + f(x_i + h) - 2 * f(x_i))/h**2)
        y_d2true.append(d2f(x_i))

        n_left = max(n_left, abs(y_left[-1] - y_true[-1]))
        n_right = max(n_right, abs(y_right[-1] - y_true[-1]))
        n_mid = max(n_mid, abs(y_mid[-1] - y_true[-1]))
        n_d2 = max(n_d2, abs(y_d2[-1] - y_d2true[-1]))

        g_left += (y_left[-1] - y_true[-1])**2 * h
        g_right += (y_right[-1] - y_true[-1])**2 * h
        g_mid += (y_mid[-1] - y_true[-1])**2 * h
        g_d2 += (y_d2[-1] - y_d2true[-1])**2 * h

    nc.append((n_left, n_right, n_mid, n_d2))
    g.append((g_left, g_right, g_mid, g_d2))
    n *= 2
print("Невязка Чебышева:")
for i in range(len(nc)):
    for j in range(len(nc[i])):
        print(f'{nc[i][j]:.4e}', end=" ")
    print('\n')
print("Невязка Гилберта:")
for i in range(len(g)):
    for j in range(len(g[i])):
        print(f'{g[i][j]:.4e}', end=" ")
    print('\n')

