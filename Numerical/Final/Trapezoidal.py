def func(x):
    return 1 / (1 + x ** 2)
    # return math.log(x)


def trapezoidal(ll, ul, n):
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
        else:
            res += 2 * fx[i]

    res = res * (h / 2)
    return res


lower_limit = 0  # Lower limit
upper_limit = 1  # Upper limit
n = 6  # Number of interval
print("%.6f" % trapezoidal(lower_limit, upper_limit, n))
