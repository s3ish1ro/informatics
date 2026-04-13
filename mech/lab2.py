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


EPS = 1e-3
E1 = 2 * 10 ** 11
E2 = 4 * 10 ** 11
E3 = 9 * 10 ** 10
P1 = 30000
P2 = 60000
P3 = 100000
n = 12
L = 3
u0 = 0.001
q = 150000
q1 = 300000
q2 = 500000
g = 9.81
U = []
legend = []
h = []
ax1 = plt.figure()
ax2 = plt.figure()
for k in range(4):
    K = np.zeros((n + 1, n + 1))
    F = np.zeros((n + 1, 1))
    x_i = np.linspace(0, L, n + 1)
    sigma = np.zeros(n + 1)
    h.append(L/n)
    for i in range(1, n):
        K[i][i - 1] = 1/integrate.quad(a, x_i[i - 1], x_i[i])[0]
        K[i][i] = -1/integrate.quad(a, x_i[i - 1], x_i[i])[0] - 1/integrate.quad(a, x_i[i], x_i[i + 1])[0]
        K[i][i + 1]  = 1/integrate.quad(a, x_i[i], x_i[i + 1])[0]
        x1 = x_i[i] - h[k]/2
        x2 = x_i[i] + h[k]/2
        # K[i][i-1] = e(x1)
        # K[i][i] = -e(x1) - e(x2)
        # K[i][i + 1] = e(x2)
        F[i][0] = g * integrate.quad(p, x1, x2)[0] - q1 * delta(x_i[i] - L/3)  - q2 * delta(x_i[i] - L/2)

    K[0][0] = 1
    K[n][n - 1] = -1/integrate.quad(a, x_i[n - 1], x_i[n])[0]
    K[n][n] = 1/integrate.quad(a, x_i[n - 1], x_i[n])[0]
    F[0][0] = -u0
    F[n][0] = q
    U.append(np.linalg.solve(K, F).transpose()[0])
    for j in range(0, len(sigma) - 1):
        sigma[j] = 1 / integrate.quad(a, x_i[j], x_i[j + 1])[0] * (U[k][j + 1] - U[k][j])
    #sigma[0] = e(x_i[0]) * (U[k][1] - U[k][0]) / h[k]
    sigma[n] = e(x_i[n]) * (U[k][n] - U[k][n - 1]) / h[k]

    plt.figure(ax1)
    plt.plot(x_i, U[k])
    plt.figure(ax2)
    plt.plot(x_i, sigma)

    legend.append(f'n = {n}')
    n *= 2

g = []
for j in range(len(U)-1):
    g0 = 0
    for i in range(len(U[j]) - 1):
        g0 += (U[j][i] - U[j+1][2 * i])**2 * h[j]
    g.append(g0)
for i in range(len(g)):
        print(f'{np.sqrt(g[i]):.3e}')

plt.xlabel('Длина стержня, м')
plt.ylabel('Напряжения, Па')
plt.ticklabel_format(axis='y', scilimits=(0, 0))
plt.legend(legend)
plt.grid()
plt.figure(ax1)
plt.xlabel('Длина стержня, м')
plt.ylabel('Перемещения, м')
plt.ticklabel_format(axis='y', scilimits=(0, 0))
plt.grid()
plt.legend(legend)
plt.show()
