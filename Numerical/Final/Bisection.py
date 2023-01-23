def func(x):
    return x**3-5*x-9


def bisection(a, b):
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    c = a

    while (a<b):

        # Find middle point
        c = (a + b) / 2

        # Check if middle point is root
        if (func(c) == 0.0):
            break

        # Decide the side to repeat the steps
        if (func(c) * func(a) < 0):
            b = c
        else:
            a = c

    print("The value of root is : ", "%.4f" % c)



a = -200
b = 300
bisection(2, 3)
