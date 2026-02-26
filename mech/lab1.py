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
EPS = 10**-2
E1 = 2 * 10**11
E2 = 2 * 10**11
E3 = 2 * 10**11
P1 = 150
P2 = 492
P3 = 732
n = 150
L = 1
u0 = 0.001
q1 = 15300
q2 = 20100
q = 13400
g = 9.81
x_i = np.linspace(0, L, n + 1)
h = L / n
K = np.zeros((n + 1, n + 1))
B = np.zeros((n + 1, 1))
for i in range(1, n):
    K[i][i - 1] = e(x_i[i - 1]) / (h ** 2)
    K[i][i] = (-e(x_i[i - 1]) - e(x_i[i])) / (h ** 2)
    K[i][i + 1] = e(x_i[i]) / (h ** 2)
    B[i][0] = p(x_i[i]) * g - q1 * delta(x_i[i] - L/3)/h - q2 * delta(x_i[i] - L/2)/h
    K[0][0] = 1
    B[0][0] = -u0
    K[n][n - 1] = -1/h
    K[n][n] = 1/h
    B[n][0] = q/e(L)


U = np.dot(np.linalg.inv(K), B)
plt.grid()
plt.plot(x_i, U)
plt.show()
