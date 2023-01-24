def func(x, y):
    return x + y + x * y


def euler(x, y, h, x_val):

    while x < x_val:
        y = y + h * func(x, y)
        x = x + h

    # Printing approximation
    print("Approximate solution at x = ", x_val, " is ", "%.6f" % y)


x0 = 0
y0 = 1
h = 0.025
x = 0.5

euler(x0, y0, h, x)
