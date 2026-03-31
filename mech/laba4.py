import numpy as np
from scipy.integrate import quad
import  matplotlib.pyplot as plt

def delta(x):
    if abs(x) <= 1e-4:
        return 1
    else:
        return 0

def E(x):
    if x <= l/3:
        return E1
    elif x <= 2 * l/3:
        return E2
    else:
        return E3


def P(x):
    if x <= l / 3:
        return P1
    elif x <= 2 * l / 3:
        return P2
    else:
        return P3


E1 = 2 * 10**11
E2 = 4 * 10**11
E3 = 8 * 10**10
P1 = 50000
P2 = 30000
P3 = 10000
n = 31
l = 3
g = 9.81
q1 = 30000
q2 = 40000
q = 25000
x = np.linspace(0, l, n)
K = np.zeros((n, n))
F = np.zeros((n, 1))
h = l/(n - 1)
for i in range(0, n - 1):
    B = [[-1/h], [1/h]]
    K_E = B @ np.transpose(B)
    D = quad(E, x[i], x[i + 1])[0]
    Fg = np.array([[P1 * g * h/2], [P1 * g * h/2]])
    Fq = np.array([[q1/2 * delta(x[i] - l/3) + q2/2 * delta(x[i] - l/2) + q * delta(x[i] - l)], [q1/2 * delta(x[i + 1] - l/3) + q2/2 * delta(x[i + 1] - 2 * l/3) + q * delta(x[i + 1] - l)]])
    F_E = Fg + Fq
    for j in range(len(K_E)):
        for k in range(len(K_E[j])):
            K[j + i][k + i] += K_E[j][k] * D
    for j in range(len(F_E)):
        F[j + i][0] += F_E[j][0]
K[1][1] *= 10**8
U = np.dot(np.linalg.inv(K), F)
sigma = np.zeros_like(U.transpose()[0])

for i in range(0, n - 1):
    U_E = [U.transpose()[0][i], U.transpose()[0][i + 1]]
    D = quad(E, x[i], x[i + 1])[0]
    B = [-1 / h, 1 / h]
    

plt.plot(x, U)
plt.grid()
plt.show()
