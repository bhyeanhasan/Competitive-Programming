def f(x):
    return 1 / (1 + x ** 2)


def simpsons_3By8(x0, xn, n):
    h = (xn - x0) / n

    x = list()
    fx = list()

    for i in range(n + 1):
        x.append(x0 + h * i)
        fx.append(f(x[i]))

    res = 0

    for i in range(n + 1):
        if i == 0 or i == n:
            res += fx[i]
        elif i % 3 == 0:
            res += 2 * fx[i]
        else:
            res += 3 * fx[i]

    res = res * 3 * h / 8

    return res


lower_limit = 0.2  # Lower limit
upper_limit = 0.8  # Upper limit
n = 2  # Number of interval
print("%.6f" % simpsons_3By8(0, 1, 6))
