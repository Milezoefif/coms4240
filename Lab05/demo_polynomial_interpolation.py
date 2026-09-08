import numpy as np

"""
look at corner
if 0, look for non-0 below
    if none found, go to next column
if non-0
    do elementary row ops
"""

def GaussElimination(A, b):
    # Add b as last column
    A = np.c_[A, b]
    print(A)
    columns = A[0].size
    rows = A.ndim

    r = 0

    for c in range(columns - 1):
        if A[r][c] == 0:
            for ri in range(r + 1, rows):
                if A[ri][c] != 0:
                    A[[r, ri], :] = A[[ri, r], :]
                    break
            if A[r][c] == 0:
                continue
        for ri in range(r + 1, rows):
            change = A[r] * (A[ri][c] / A[r][c])
            if A[ri][c] > 0 == change[ri][c] > 0:
                change = -change
            A[ri] += change
        r += 1

    print(A)

    result = np.array([])
    for ri in range(rows):
        result = np.append(result, A[ri][columns - 1])
    return result

A = np.array([[-4.3, 7.1], [-0.2, 5.6]])
b = np.array([-44.1, -28.4])

x = GaussElimination(A, b)
#print(x) # [ 2. -5.]