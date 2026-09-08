import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Return performance metrics for using pop() operations on the end vs beginning of a list
def profile_pop(L):
    l1 = list(L)
    l2 = list(L)

    start1 = time.perf_counter()
    l1.pop()
    end1 = time.perf_counter()
    time1 = end1 - start1

    start2 = time.perf_counter()
    l2.pop(0)
    end2 = time.perf_counter()
    time2 = end2 - start2

    #print(f"L.pop(): {time1}\nL.pop(0): {time2}\n")
    return [time1, time2]

# Return performance metrics for using in-order vs out-of-order reverse operations
def profile_reverse(L):
    l1 = list(L)
    l2 = list(L)

    start1 = time.perf_counter()
    l1.reverse()
    end1 = time.perf_counter()
    time1 = end1 - start1

    start2 = time.perf_counter()
    R = l2[::-1]
    end2 = time.perf_counter()
    time2 = end2 - start2

    #print(f"L.reverse(): {time1}\nR = L[::-1]: {time2}\n")
    return [time1, time2]

N = 17

lpop = [0] * N
lpopz = [0] * N
lreverse = [0] * N
rreverse = [0] * N

"""
For a random list L of size N, where N is {2^0, 2^1, ..., 2^16}, we run the
above profiling methods an arbitrarily large number of times (100 in this case).
This is to generalize the output and hopefully minimize variance in the results.
"""
for i in range(N):
    n = 2 ** i
    L = [random.random() for _ in range(n)]
    it = 100
    val = 0
    for j in range(it):
        l = profile_pop(L)
        lpop[i] += l[0]
        lpopz[i] += l[1]
        l = profile_reverse(L)
        lreverse[i] += l[0]
        rreverse[i] += l[1]
    lpop[i] = lpop[i] / it
    lpopz[i] = lpopz[i] / it
    lreverse[i] = lreverse[i] / it
    rreverse[i] = rreverse[i] / it

fig, axis = plt.subplots(1, 2)
# Plot performance comparison of L.pop() and L.pop(0)
axis[0].plot(np.arange(0, N), lpop, label='L.pop()')
axis[0].plot(np.arange(0, N), lpopz, label='L.pop(0)')
axis[0].set_title("L.pop() vs L.pop(0)")
axis[0].set(xticks=np.arange(0, N), xlabel='N = 2^X', ylabel='Execution Time')
axis[0].legend()

# Plot performance comparison of L.reverse() and R = L[::-1]
axis[1].plot(np.arange(0, N), lreverse, label='L.reverse()')
axis[1].plot(np.arange(0, N), rreverse, label='N = L[::-1]')
axis[1].set_title("L.reverse() vs N = L[::-1]")
axis[1].set(xticks=np.arange(0, N), xlabel='N = 2^X', ylabel='Execution Time')
axis[1].legend()

plt.show()