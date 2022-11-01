import math
import numpy as np
from math import ceil


def phi(x: float, R) -> float:
    if -math.pi * R / 2 <= x <= math.pi * R / 2:
        return 1
    return 0


def get_sol(u, arr, value, fixed):
    h = arr[1] - arr[0]
    j = ceil(value / h)
    if fixed == 'x':
        a = np.copy(u[:, j])
    else:
        a = np.copy(u[j, :])
    return a


def solution(const_k, c, R, x: [float], t: [float]):
    I = len(x) - 1
    K = len(t) - 1
    h_x = x[1] - x[0]
    h_t = t[1] - t[0]
    gamma = (const_k * h_t) / (c * h_x ** 2)
    u = np.zeros((K + 1, I + 1), dtype=float)
    for i in range(0, I + 1):
        u[0][i] = phi(x[i], R)

    for k in range(0, K):
        for i in range(1, I):
            u[k + 1][i] = u[k][i] + gamma * (u[k][i + 1] - 2 * u[k][i] + u[k][i - 1])
    for k in range(1, K + 1):
        u[k][I] = (u[k][1] - u[k][I - 1]) / 2
        u[k][0] = u[k][I]
    return u


def get_numerical(k, c, R, T, X_value, x_array, t_array):
    u = solution(k, c, R, x_array, t_array)
    return get_sol(u, t_array, T, 't'), get_sol(u, x_array, X_value, 'x')
