import numpy as np
import scipy.linalg


def cremar(mat, const):
    D = np.linalg.det(mat)
    x = np.linalg.det([const, mat[:, 1], mat[:, 2]]) / D
    y = np.linalg.det([mat[:, 0], const, mat[:, 2]]) / D
    z = np.linalg.det([mat[:, 0], mat[:, 1], const]) / D
    return x, y, z


a = np.array([[6, 3, 4],
              [3, 6, 5],
              [4, 5, 10]])

b = np.array([2, -3, 6])

p, l, u = scipy.linalg.lu(a)

ans = cremar(l,b)
ans = cremar(u,ans)

print(ans)

