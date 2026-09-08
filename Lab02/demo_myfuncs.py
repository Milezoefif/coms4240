e = 2.7182818284590451

def fac(n):
    n = int(n)
    s = 1
    for i in range(1, n):
        s = s * (i + 1)
    return s

def sqrt(x, kmax=100):
    x = float(x)
    s = 1.0
    for i in range(kmax):
        s = 0.5 * (s + (x / s))
    return s

def exp(x, deg=100):
    x = float(x)
    x0 = int(round(x))
    z = x - x0

    c = 1.0
    for d in range(1, deg):
        c += (z ** d) / fac(d)
    return (e ** x0) * c

def ln(x, kmax=100):
    x = float(x)
    s = 1.0
    for i in range(kmax):
        s = s - 1 + x * exp(-s)
    return s

x = input("Enter a number for x!: ")
y = fac(x)
print(f"{x}!: {y}\n")

x = input("Enter a number for sqrt(x): ")
y = sqrt(x)
print(f"sqrt({x}): {y}\n")

x = input("Enter a number for e^x: ")
y = exp(x)
print(f"e^{x}: {y}\n")

x = input("Enter a number for ln(x): ")
y = ln(x)
print(f"ln({x}): {y}\n")
