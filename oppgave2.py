from typing_extensions import Never
import numpy as np


def oppgave2_a():
    n = int(100000)
    i = int(99940)
    k = int(1)
    teller = int(1)
    nevner = np.math.factorial(i)
    for k in range(1, i+1):
        teller = (n-k+1)*teller
    print(teller/nevner)


def oppgave_2b():
    n = float(1000)
    i = 500
    h = float(1)
    for j in range(1, int(i+1)):
        j = float(j)
        h *= ((n-j+1)/j)
    print(h)

#--------------------------------oppgave 2b--------------------------------#


"""
a = (5000-1+1)*(4999-2+1)*(4998-3+1)*(4997-4+1)
b = 4*3*2*1

g = np.math.factorial(5000)
k = np.math.factorial(4)
l = (5000-4)
b = np.math.factorial(l)


x = g/(k*b)
"""
