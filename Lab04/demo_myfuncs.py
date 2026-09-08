import matplotlib.pyplot as plt

e = 2.7182818284590451

def fac(n):
    n = float(n)
    if n < 0:
        print("Cannot provide negative numbers as input to fac()")
        return
    if n - int(n) != 0:
        print("Cannot provide non-integer values as input to fac()")
        return
    n = int(n)
    s = 1
    for i in range(1, n):
        s = s * (i + 1)
    return s

def sqrt(x, init=1.0, kmax=100, tol=10e-18):
    x = float(x)
    if x < 0:
        print("Cannot provide negative numbers as input to sqrt()")
        return
    if x == 0:
        return 0
    s = init
    for i in range(kmax):
        old = s
        s = 0.5 * (s + (x / s))
        if abs(old - s) / x < tol:
            print(f"sqrt iterations: {i}")
            break
    return s

def exp(x, deg=100, tol=10e-18, log=True):
    x = float(x)
    if x == 0:
        return 0
    x0 = int(round(x))
    z = x - x0
    c = 1.0
    for d in range(1, deg):
        old = c
        c += (z ** d) / fac(d)
        if abs(old - c) / abs(x) < tol:
            if log: print(f"exp iterations: {d}")
            break
    return (e ** x0) * c

def ln(x, init=1.0, kmax=100, tol=10e-18):
    x = float(x)
    if x < 0:
        print("Cannot provide negative numbers as input to ln()")
        return
    if x == 0:
        return 0
    s = init
    for i in range(kmax):
        old = s
        s = s - 1 + x * exp(-s, log=False) # log=False, prevents exp() from printing iteration numbers on calls to ln()
        if abs(old - s) / x < tol:
            print(f"ln() iterations: {i}")
            break
    return s

def population_exact(t, r=0.5, K=100, P_init=10):
    if r <= 0:
        print("r must be > 0")
        return
    if K <= 0:
        print("K must be > 0")
        return
    if P_init < 0 or P_init >= K:
        print("0 < P_0 < K must be true")
        return
    result = []
    for time in t:
        pt = P_init
        if time != 0:
            pt = K / (1 + ((K - P_init) / P_init) * exp(-r * time))
        result.append(pt)
    return result

def population_approximate(t, r=0.5, K=100, P_init=10):
    if r <= 0:
        print("r must be > 0")
        return
    if K <= 0:
        print("K must be > 0")
        return
    if P_init < 0 or P_init >= K:
        print("0 < P_0 < K must be true")
        return
    P = P_init
    result = [P]
    for i in range(1, t + 1):
        P = P + (r * P * (1 - P / K))
        result.append(P)
    return result



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

# Testing population growth functions and plot comparison
# Values here are hardcoded for t = [0, 1, ..., 20]
x = range(0, 21)
pop_e = population_exact(x)

x = 20
pop_a = population_approximate(x)

plt.plot(range(0, 21), pop_e, label='Exact')
plt.plot(range(0, 21), pop_a, label='Approximate')
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.show()

