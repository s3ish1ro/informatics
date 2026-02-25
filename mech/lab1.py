import matplotlib.pyplot as plt
import numpy as np

def e(x, l=5):
    if x <= l/3:
        return E1
    elif l/3 < x <= 2 * l/3:
        return E2
    else:
        return E3

def p(x, l=5):
    if x <= l/3:
        return P1
    elif l/3 < x <= 2 * l/3:
        return P2
    else:
        return P3
E1 = 20
E2 = 20
E3 = 20
P1 = 50
P2 = 50
P3 = 50
n = 30
L = 5
u0 = 10
q1 = 15
q2 = 20
q = 10
g = 9.81
A = 2
x_i = np.linspace(0, L, n)
h = L/n
K = np.zeros((n + 1, n + 1))
B = np.zeros((n + 1, 1))
for i in range(1, n):
    K[i][i-1] = e(x_i[i - 1]) / (h**2)
    K[i][i] = ( -e(x_i[i - 1]) - e(x_i[i])) / (h**2)
    K[i][i + 1] = e(x_i[i]) / (h**2)
    B[i][0] = p(x_i[i]) * g / A
    
