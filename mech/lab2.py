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
    elif L / 3 < x <= 2 * L / 3:
        return P2
    else:
        return P3

def delta(x,x0):
    if abs(x-x0) <= EPS:
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


EPS = 10**-6
E1 = 3 * 10 ** 11
E2 = 4 * 10 ** 11
E3 = 6 * 10 ** 11
P1 = 5000
P2 = 15000
P3 = 10000
n = 100
L = 6
u0 = 0.001
q = 10000
q1 = 50000
q2 = 30000
g = 9.81
U = np.zeros(n + 1)
K = np.zeros((n + 1, n + 1))
F = np.zeros((n + 1, 1))
x_i = np.linspace(0, L,2 * n + 1)
sigma = np.zeros(n + 1)
h = L/n

for i in range(1, n):
    K[i][i - 1] = 1/integrate.quad(a, x_i[2 * (i - 1)], x_i[2 * i])[0]
    K[i][i] = -1/integrate.quad(a, x_i[2 * (i - 1)], x_i[2 * i])[0] - 1/integrate.quad(a, x_i[2 * i], x_i[2 * (i + 1)])[0]
    K[i][i + 1]  = 1/integrate.quad(a, x_i[2 * i], x_i[2 * (i + 1)])[0]
    F[i][0] = g * integrate.quad(p, x_i[i - 1], x_i[i + 1])[0] - q1/h * (hev(x_i[i + 1] - L/3) - hev(x_i[i - 1] - L/3)) - q2/h * (hev(x_i[i + 1] - L/2) - hev(x_i[i - 1] - L/2))

K[0][0] = 1

K[n][n - 1] = -1/integrate.quad(a, x_i[2 * (n - 1)], x_i[2 * n])[0]
K[n][n] = 1/integrate.quad(a, x_i[2 * (n - 1)], x_i[2 * n])[0]

F[0][0] = -u0
F[n][0] = q/e(x_i[n])
U = np.dot(np.linalg.inv(K), F)
for i in range(1, n):
    sigma[i] = e(x_i[2 * i]) * (U[i + 1][0] - U[i][0])/h
sigma[0] = e(x_i[0]) * (U[1][0] - U[0][0])/h
sigma[n] = e(x_i[n]) * (U[n][0] - U[n - 1][0])/h
plt.plot(x_i[0:2 * n + 1:2], U.transpose()[0])

plt.grid()
plt.show()
plt.plot(x_i[0:2 * n + 1:2], sigma)
plt.grid()
plt.show()
