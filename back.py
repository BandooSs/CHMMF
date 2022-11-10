import math
import numpy as np
import analytical
import matplotlib.pyplot as plt
from numerical import get_numerical

const_k = 0.59
c = 1.65
R = 5
T = 180
s = 0.04
L = 2 * math.pi * R
eps = 0.0001
a = []
b = []
eps_x = []


def create_plot(title, label):
    fig, ax = plt.subplots()
    ax.grid()
    ax.set_title(title)
    ax.set_xlabel(label)
    ax.set_ylabel('U(x,t)')
    return ax


def dynamic(el, ky):
    I_array = 60
    K_array = 3000
    ax3 = create_plot(f't', 'x')
    ax4 = create_plot(f'x', 't')

    x_array = np.linspace(-math.pi * R, math.pi * R, I_array)
    t_array = np.linspace(0, T, K_array)
    t = np.arange(0, T + T / 5, T / 5)
    a = [4, 2, 1, -2, -4, -1]
    for i, j in zip(t, a):
        x, t = get_numerical(const_k, c, R, i, -math.pi * R / j, x_array, t_array, el, ky)
        ax3.plot(x_array, np.abs(x), linestyle='-', label=f't={i}')
        ax4.plot(t_array, np.abs(t), linestyle='-', label=f'x=pi*R/{j}')
        print(i, " ", j)
    print(t)

    ax3.legend()
    ax4.legend()
    plt.show()


def convergence(I_array, K_array, x_val1, t_val, el, ky):
    x_array = np.linspace(-math.pi * R, math.pi * R, 500)
    t_array = np.linspace(0, T, 500)
    global a, b, eps_x
    x_val = math.pi * R * x_val1
    y_1, y_2 = analytical.get_analutical(const_k, c, R, t_val, x_val, x_array, t_array, eps)
    ax1 = create_plot(f't={t_val}', 'x')
    ax2 = create_plot(f'x=pi * R * {x_val1}', 't')
    ax1.plot(x_array, np.abs(y_1), label='analytical')
    ax2.plot(t_array, np.abs(y_2), label='analytical')
    num_array = []
    an_array = []

    for i, k in zip(I_array, K_array):
        x_array = np.linspace(-math.pi * R, math.pi * R, i)
        t_array = np.linspace(0, T, k)
        x, t = get_numerical(const_k, c, R, t_val, x_val, x_array, t_array, el, ky)
        num_array.append(x)
        y1, y2 = analytical.get_analutical(const_k, c, R, t_val, x_val, x_array, t_array, eps)
        an_array.append(y1)
        ax1.plot(x_array, np.abs(x), linestyle='--', label=f'k={k} i= {i}')
        ax2.plot(t_array, np.abs(t), linestyle='--', label=f'k={k} i= {i}')

    a.append(np.max(np.abs(num_array[0] - an_array[0])))
    for i in range(0, len(I_array) - 1):
        b.append(np.max(np.abs(num_array[i + 1] - an_array[i + 1])))
        eps_x.append(a[i] / b[i])
        if len(a) != len(I_array) - 1:
            a.append(b[i])

    ax1.legend()
    ax2.legend()
    plt.show()
