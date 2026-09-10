import numpy as np
import matplotlib.pyplot as plt

def GaussElimination(A, b):
    A = A.astype(np.float32)
    b = b.astype(np.float32)
    # Add b as last column
    A = np.c_[A, b]

    columns = A[0].size
    rows = len(A)

    r = 0

    # Create triangular form
    for c in range(columns - 1):
        # Find non-zero pivot point
        if A[r][c] == 0:
            for ri in range(r + 1, rows):
                if A[ri][c] != 0:
                    A[[r, ri], :] = A[[ri, r], :]
                    break
            if A[r][c] == 0:
                continue

        # Set pivot equal to 1
        scalar = A[r][c]
        for ci in range(columns):
            A[r][ci] = A[r][ci] / scalar

        # Make all values above and below pivot into 0's
        for ri in range(rows):
            if ri == r: continue
            # row * scalar to create 0 at row ri
            change = A[r] * (A[ri][c] / A[r][c])
            # Flip sign of added row if needed
            if (A[ri][c] > 0) == (change[c] > 0):
                change = -change
            A[ri] += change

        r += 1

    result = np.array([])
    for ri in range(rows):
        # Check if system has no solution
        for ci in range(columns - 1):
            if A[ri][ci] != 0: break
            if ci == columns - 2:
                print("No solution exists for given A and b")
                return
        result = np.append(result, A[ri][columns - 1])
    return result

"""
x - vector of inputs of given data
f - vector of outputs of the function f(x) from the given data
n - maximum size of the desired polynomial
"""
def LeastSquareApprox(x, f, n):
    # Create matrix X of size (x inputs) * (size of desired polynomial + 1)
    X = np.ones((len(x), n + 1))
    # Construct matrix of the form [1, x_0, x_0^2, x_0^3, ..., x_0^n] for each element in x
    for i in range(1, n + 1):
        X[:,i] = x ** i

    XtX = np.transpose(X) @ X
    Xtf = np.transpose(X) @ f

    a = GaussElimination(XtX, Xtf)
    return a

if __name__ == "__main__":
    xgrid = np.linspace(-np.pi, np.pi, 51)
    fx = np.cos(xgrid)

    n = 5
    coef = LeastSquareApprox(xgrid, fx, n)

    px = np.array([])
    for x in xgrid:
        # Find value of p(x) at each element in x
        p = 0
        for i in range(n):
            p += coef[i] * (x ** i)
        px = np.append(px, p)

    plt.plot(xgrid, fx, label="cos(x)")
    plt.plot(xgrid, px, label="p(x)")
    plt.xlabel("x")
    plt.legend()
    plt.savefig("fx-and-px-plot")