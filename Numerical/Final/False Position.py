MAX_ITER = 1000000


def func(x):
    return x ** 3 - 0.165 * x ** 2 + 3.993 * (1 / 10000)


def FalsePosition(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c = a

    for i in range(MAX_ITER):

        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        if func(c) == 0:
            print(c)
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
    print("The value of root is : ", '%.4f' % c)


a = 0
b = 0.11
FalsePosition(a, b)
