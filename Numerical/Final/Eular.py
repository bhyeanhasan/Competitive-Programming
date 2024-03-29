import numpy as np
import math
def func(x, y):
    return math.exp(x/2)*math.sin(5*x)


def euler(x, y, h, x_val):

    n = int(x_val/h)

    for i in range(n):
        y = y + h * func(x, y)
        x = x + h

    # Printing approximation
        print("Approximate solution at x = ", x, " is ", "%.6f" % y)


x0 = 0
y0 = 0
h = 0.1
x = 1

euler(x0, y0, h, x)

