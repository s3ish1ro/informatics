import matplotlib.pyplot as plt
import numpy as np


def e(x):
    if x <= L / 3:
        return E1
    elif L / 3 < x <= 2 * L / 3:
        return E2
    else:
        return E3


def p(x):
    if x <= L / 3:
        return P1
    elif L / 3 < x <= 2 * L / 3:
        return P2
    else:
        return P3

def delta(x):
    if abs(x) <= EPS:
        return 1
    else:
        return 0
EPS = 10**-3
E1 = 2.1 * 10 ** 11
E2 = 3 * 10 ** 11
E3 = 4 * 10 ** 11
P1 = 5000
P2 = 5000
P3 = 5000
n = 100
L = 4
u0 = 0.001
q = 2500
q1 = 10000
q2 = 30000
g = 9.81
U = []
legend = []
h = []
ax, surf = plt.subplots(1, 2)
for k in range(4):
    x_i = np.linspace(0, L, n + 1)
    h.append(L / n)
    K = np.zeros((n + 1, n + 1))
    B = np.zeros((n + 1, 1))
    sigma = np.zeros(n + 1)
    for i in range(1, n):
        K[i][i - 1] = e(x_i[i - 1]) / (h[k] ** 2)
        K[i][i] = (-e(x_i[i - 1]) - e(x_i[i])) / (h[k] ** 2)
        K[i][i + 1] = e(x_i[i]) / (h[k] ** 2)
        B[i][0] = p(x_i[i]) * g - q1 * delta(x_i[i] - L/3)/h[k] - q2 * delta(x_i[i] - L/2)/h[k]

    K[0][0] = 1
    B[0][0] = -u0
    K[n][n - 1] = -1/h[k]
    K[n][n] = 1/h[k]
    B[n][0] = q/e(L)
    U.append(np.linalg.solve(K, B))
    for i in range(1, n):
        sigma[i] = e(x_i[i]) * (U[k][i+1][0] - U[k][i][0]) / h[k]
    sigma[0] = e(x_i[0]) * (U[k][1][0] - U[k][0][0]) / h[k]
    sigma[n] = e(x_i[n]) *(U[k][n][0] - U[k][n-1][0]) / h[k]
    surf[0].plot(x_i, U[k].transpose()[0])
    surf[1].plot(x_i, sigma)
    legend.append(f'n = {n}')
    n *= 2
g = []
for j in range(len(U)-1):
    g0 = 0
    for i in range(len(U[j]) - 1):
        g0 += (U[j][i][0] - U[j+1][2 * i][0])**2 * h[j]
    g.append(g0)
for i in range(len(g)):
    print(f'{np.sqrt(g[i]):.3e}')
surf[0].legend(legend)
surf[1].legend(legend)
surf[0].grid()
surf[1].grid()
surf[0].set_xlabel('Длина балки, м')
surf[1].set_xlabel('Длина балки, м')
surf[0].set_ylabel('Перемещения, м')
surf[1].set_ylabel('Напряжения, Па')

plt.show()
