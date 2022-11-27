
import numpy as np
import sys

# n = int(input('Enter number of unknowns: '))
n=3
# a = np.zeros((n, n + 1))
x = np.zeros(n)

a = np.array([[3, -0.1, -0.2, 7.85],
              [0.1, 7, -0.3,-19.3],
              [0.3, -0.2, 10,71.4]])

#x = np.array([7.85, -19.3, 71.4])
# print('Enter Augmented Matrix Coefficients:')
# for i in range(n):
#     for j in range(n + 1):
#         a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(n):
        if i != j:
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]


for i in range(n):
    x[i] = a[i][n] / a[i][i]

print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')