import numpy as np


def gaussElim(a):
    n = 3

    for i in range(n - 1):
        if a[i][i] == 0.0:
            print('Divide by zero detected!')

        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    print('After forward elimination: ')
    print(a)

    valu = a[0:n, n]
    # forward subtraction
    for k in range(n - 1, -1, -1):
        valu[k] = (valu[k] - np.dot(a[k, k + 1:n], valu[k + 1:n])) / a[k, k]

    return valu


a = np.array([[3, -0.1, -0.2, 7.85],
              [0.1, 7, -0.3, -19.3],
              [0.3, -0.2, 10, 71.4]])

x = gaussElim(a)

print(x)
