import numpy as np

# n = int(input('No of Unknown Variable: '))
# arr = np.zeros((n, n + 1))
#
# for i in range(n):
#     row = list(map(int, input('Enter Equation ' + str(i + 1) + ' : ').split()))
#     arr[i] = row

arr = np.array([[3, -0.1, -0.2, 7.85],
                [0.1, 7, -0.3, -19.3],
                [0.3, -0.2, 10, 71.4]])
n = 3


Matrix = arr[0:n, 0:n]
Valu = arr[0:n, n]


D = np.linalg.det(Matrix)

result = []

for i in range(n):
    flag = Matrix.copy()
    flag[0:n, i] = Valu
    d = np.linalg.det(flag)
    d = d / D
    result.append(d)

print(*result)

'''
3
10 40 70 300
20 50 80 360
30 60 80 390
'''
