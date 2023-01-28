def func(x, y):
    return x-y


def euler(x, y, h, x_val):

    n = int(x_val/h)

    for i in range(n):
        y = y + h * func(x, y)
        x = x + h

    # Printing approximation
        print("Approximate solution at x = ", x, " is ", "%.6f" % y)


x0 = 0
y0 = 1
h = 0.2
x = 2

euler(x0, y0, h, x)

