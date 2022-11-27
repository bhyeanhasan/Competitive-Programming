import numpy as np
import sys

a = np.array([[6, 3, 4, 2], [3, 6, 5, -3], [4, 5, 10, 6]])
print(a)
n = 3
# x = np.zeros(n)
# n = int(input('Enter number of unknowns: '))
# a = np.zeros((n, n + 1))
x = np.zeros(n)
# # input fron keybord
# print('Enter Augmented Matrix Coefficients:')
# for i in range(n):
#     for j in range(n + 1):
#         a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

# Applying Gauss Elimination
for i in range(n):  # row wise work
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]

        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution
x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]

    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]

    x[i] = x[i] / a[i][i]

# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')

# 3
# 6 3 4 2
# 3 6 5 -3
# 4 5 10 6