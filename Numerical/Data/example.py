import numpy as np


def gaussElim(a):
    n = 3
    for i in range(n - 1):
        for j in range(i + 1, n):
            flag = a[j, i] / a[i, i]
            for row in range(n + 1):
                a[j, row] = a[j, row] - (a[i, row] * flag)
    print(a)
    result = []

    for i in range(n - 1, -1, -1):
        x = a[i][i + 1] - np.dot(a[i,i+1:n],) / a[i][i]


        result.append(x)
    print(result)


a = np.array([[10, 40, 70, 300],
              [20, 50, 80, 360],
              [30, 60, 80, 390]])
gaussElim(a)
