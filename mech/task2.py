import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x
def p(x):
    return -1/x
def solve(x):
    return x**3/3 - x**2 + 2/3
a = 1
b = 2
n = 100
y = []
h = []
for k in range(4):
    K = np.zeros((n + 1, n + 1))
    B = np.zeros((n + 1, 1))
    x_i = np.linspace(a, b, n + 1)
    h.append((b - a)/n)
    for i in range(1 , n):
        K[i][i - 1] = (1/h[k]**2) - (p(x_i[i])/h[k])
        K[i][i] = (-2/h[k]**2) + p(x_i[i])/h[k]
        K[i][i + 1] = 1/h[k]**2
        B[i][0] = f(x_i[i])
    K[0][0] = 1
    K[n][n-1] = -1/h[k]
    K[n][n] = 1/h[k]
    y.append(np.dot(np.linalg.inv(K), B))
    n *= 2
    plt.plot(x_i, y[k].transpose()[0])

g = []
for j in range(len(y)-1):
    g0 = 0

    for i in range(len(y[j])):
        g0 += (y[j][i] - y[j+1][2 * i])**2 * h[j + 1]
    g.append(g0)
for i in range(len(g)):
    print(f'{np.sqrt(g[i][0]):.3e}')


# plt.plot(x_i, solve(x_i), color="black")
plt.grid()
plt.show()

