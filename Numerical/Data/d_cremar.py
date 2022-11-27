from numpy import array, zeros, sqrt, linalg


def symmetric(A):
    return (A == A.T).all()

def positiveDefinite(A):  # for i in range(len(matrix)):
    E = linalg.eigvals(A)  # if E[i] < 0: return False
    return (E >= 0).all()  # return True


def decomposition(A):
    N = len(A)
    L = zeros((N, N))  # L = zeros_like(A)

    for j in range(N):  # j = 0 to N-1
        for i in range(j, N):  # i = j to N-1
            if i == j:
                L[i, j] = sqrt(A[i, j] - sum(L[i, :j] ** 2))  # k = 0 to j-1
            else:
                L[i, j] = (A[i, j] - sum(L[i, :j] * L[j, :j])) / L[j, j]

    print('Cholesky Decomposition:')
    print('[L] =\n', L, sep='', end='\n\n')
    return L


def solveCholesky(A, B):
    L = decomposition(A)
    U = L.T
    N = len(L)

    X = zeros(N)
    Y = zeros(N)

    # Forward Substitution
    for i in range(N):  # i = 0 to N-1
        Y[i] = (B[i] - sum(L[i, :i] * Y[:i])) / L[i, i]  # j = 0 to i-1

        # sumj = 0
        # for j in range(i):
        #     sumj += L[i,j] * Y[j]
        # Y[i] = (B[i] - sumj) / L[i,i]

    # Backward Substitution
    for i in range(N - 1, -1, -1):  # i = N-1 to 0
        X[i] = (Y[i] - sum(U[i, i + 1:] * X[i + 1:])) / U[i, i]  # j = i+1 to N-1

        # sumj = 0
        # for j in range(i+1, N):
        #     sumj += U[i,j] * X[j]
        # X[i] = (Y[i] - sumj) / U[i,i]

    return X


# System of Equations

A = array([[6, 15, 55],
           [15, 55, 225],
           [55, 225, 979]], float)
B = array([-19, -100, -474], float)

N = len(A)

if symmetric(A) and positiveDefinite(A):
    X = solveCholesky(A, B)

    print("The Solution of the System:")
    for i in range(N):
        print('X[', i + 1, '] = ', round(X[i], 6), sep='')
else:
    print("The System cannot be Solved by Cholesky Decomposition")