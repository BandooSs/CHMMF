import math
import numpy as np
import analytical
import matplotlib.pyplot as plt
from numerical import get_numerical

const_k = 0.59
c = 1.65
R = 5.0
alpha = 0.004
T = 180
s = 0.04
L = 2 * math.pi * R
eps = 0.00001


def create_plot(title, label):
    fig, ax = plt.subplots()
    ax.grid()
    ax.set_title(title)
    ax.set_xlabel(label)
    ax.set_ylabel('U(x,t)')
    return ax


if __name__ == '__main__':
    x_array = np.linspace(-math.pi * R, math.pi * R, 500)
    t_array = np.linspace(0, T, 500)
    I_array = [20, 40, 80, 120, 200]
    K_array = [600, 1200, 2400, 9600, 60000]
    t_val = T
    x_val = math.pi * R
    y_1, y_2 = analytical.get_analutical(const_k, c, R, t_val, x_val, x_array, t_array, eps)
    ax1 = create_plot(f't={t_val}', 'x')
    ax2 = create_plot(f'x={x_val:.4}', 't')
    ax1.plot(x_array, y_1, label='analytical')
    ax2.plot(t_array, y_2, label='analytical')
    for i, k in zip(I_array, K_array):
        x_array = np.linspace(-math.pi * R, math.pi * R, i)
        t_array = np.linspace(0, T, k)
        x, t = get_numerical(const_k, c, R, t_val, x_val, x_array, t_array)
        ax1.plot(x_array, x, linestyle='--', label=f'I={i} K={k}')
        ax2.plot(t_array, t, linestyle='--', label=f'I={i} K={k}')

    ax1.legend()
    ax2.legend()
    plt.show()
