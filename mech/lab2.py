import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

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
    elif L / 3 < x <= (2 * L) / 3:
        return P2
    else:
        return P3

def delta(x):
    if abs(x) <= EPS:
        return 1
    else:
        return 0
def a(x):
    return 1/e(x)
def hev(x):
    if x >= 0:
        return 1
    else:
        return 0


EPS = 10**-3
E1 = 2 * 10 ** 11
E2 = 8 * 10 ** 11
E3 = 8 * 10 ** 10
P1 = 60000
P2 = 60000
P3 = 60000
n = 20
L = 6
u0 = 0.001
q = 15000
q1 = 0
q2 = 0
g = 9.81
U = np.zeros(n + 1)
K = np.zeros((n + 1, n + 1))
F = np.zeros((n + 1, 1))
x_i = np.linspace(0, L, n + 1)
sigma = np.zeros(n + 1)
h = L/n
for i in range(1, n):
    K[i][i - 1] = integrate.quad(a, x_i[i - 1], x_i[i])[0]/h
    K[i][i] = integrate.quad(a, x_i[i - 1], x_i[i])[0]/h - integrate.quad(a, x_i[i], x_i[i + 1])[0]/h
    K[i][i + 1]  = integrate.quad(a, x_i[i], x_i[i + 1])[0]/h
    x1 = x_i[i] - h/2
    x2 = x_i[i] + h/2
    # K[i][i-1] = e(x1)
    # K[i][i] = -e(x1) - e(x2)
    # K[i][i + 1] = e(x2)
    F[i][0] = g * integrate.quad(p, x1, x2)[0] - q1 * (hev(x2 - L/3) - hev(x1 - L/3))  - q2 * (hev(x2 - L/2) - hev(x1 - L/2))

K[0][0] = 1
K[n][n - 1] = -1/integrate.quad(a, x_i[n - 1], x_i[n])[0]
K[n][n] = 1/integrate.quad(a, x_i[n - 1], x_i[n])[0]
F[0][0] = -u0
F[n][0] = q/e(x_i[n])
U = np.linalg.solve(K, F)
print(U)
for i in range(1, n):
    sigma[i] = e(x_i[i]) * (U[i + 1][0] - U[i][0])/h
sigma[0] = e(x_i[0]) * (U[1][0] - U[0][0])/h
sigma[n] = e(x_i[n]) * (U[n][0] - U[n - 1][0])/h
plt.plot(x_i, U.transpose()[0])

plt.grid()
plt.show()
plt.plot(x_i, sigma)
plt.grid()
plt.show()
