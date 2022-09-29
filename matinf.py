import numpy as np
import matplotlib.pyplot as plt

# oppgave 1
n = 1
n_next = 1
x = [n, n_next]


def sequance():
    for i in range(100):
        x.append(6*x[i+1]-3*x[i])
    # print(x)


sequance()

# oppgave 1b
n_b = 1
n_next_b = 3-np.sqrt(6)
x_b = [n_b, n_next_b]


def sequance_b():
    for i in range(100):
        x_b.append(6*x_b[i+1]-3*x_b[i])
    print(x_b)


sequance_b()
