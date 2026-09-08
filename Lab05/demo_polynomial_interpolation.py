import numpy as np

def GaussElimination(A, b):
    A = A.astype(np.float32)
    b = b.astype(np.float32)
    # Add b as last column
    A = np.c_[A, b]
    print(f"{A}\n")

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
                    print(f"{A}\n")
                    break
            if A[r][c] == 0:
                continue

        # Set pivot equal to 1
        scalar = A[r][c]
        for ci in range(columns):
            A[r][ci] = A[r][ci] / scalar

        print(f"{A}\n")

        # Make all values above and below pivot into 0's
        for ri in range(rows):
            if ri == r: continue
            # row * scalar to create 0 at row ri
            change = A[r] * (A[ri][c] / A[r][c])
            # Flip sign of added row if needed
            if (A[ri][c] > 0) == (change[c] > 0):
                change = -change
            A[ri] += change

        print(f"{A}\n")

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

A = np.array([[(-0.1) ** 3, (-0.1) ** 2, -0.1, 1], [(-0.02) ** 3, (-0.02) ** 2, -0.02, 1], [0.1 ** 3, 0.1 ** 2, 0.1, 1], [0.02 ** 3, 0.02 ** 2, 0.02, 1]])
b = np.array([np.cos(-0.1), np.cos(-0.02), np.cos(0.1), np.cos(0.02)])

x = GaussElimination(A, b)
print(f"GaussElimination(A, b): \n{x}\n")
print("The cubic polynomial which interpolates f(x) = cos(x):")
print(f"p(x) = ({x[0]})x^3 + ({x[1]})x^2 + ({x[2]})x + ({x[3]})")
