from linalg.matrix import Matrix
from linalg.create import zeroes

def make_householder():
    ...

def lu(mat: "Matrix") -> ("Matrix", "Matrix", "Matrix", int):
    """implements LUP decomposition 

    :return: returns a tuple with L, U, and P
    :rtype: "Matrix", "Matrix", "Matrix", int
    """
    assert mat._is_square()

    n = mat.shape[0]

    L, U = zeroes(n, n), zeroes(n, n)
    P, S = mat._pivotize()
    A2 = P @ mat

    for j in range(n):
        L[j][j] = 1
        for i in range(j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A2[i][j] - s1
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (A2[i][j] - s2) / U[j][j]

    return L, U, P, S

