import math


def func(x):
    return 0.2 + 25 * x - 200 * x ** 2 + 675 * x ** 3 - 900 * x ** 4 + 400 * x ** 5
    # return math.log(x)


def simpsons_1By3(ll, ul, n):
    h = (ul - ll) / n
    x = list()
    fx = list()

    for i in range(n + 1):
        x.append(ll + i * h)
        fx.append(func(x[i]))

    res = 0

    for i in range(n + 1):
        if i == 0 or i == n:
            res += fx[i]
        elif i % 2 == 0:
            res += 2 * fx[i]
        else:
            res += 4 * fx[i]

    res = res * (h / 3)
    return res


lower_limit = 0.2  # Lower limit
upper_limit = 0.8  # Upper limit
n = 2  # Number of interval
print("%.6f" % simpsons_1By3(lower_limit, upper_limit, n))
