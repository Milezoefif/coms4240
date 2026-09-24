import numpy as np
import matplotlib.pyplot as plt

with open("poly.data", "r") as data_file:
    num_points = int(data_file.readline())
    x = np.zeros(num_points)
    y = np.zeros(num_points)
    for i in range(num_points):
        str = data_file.readline()
        XnY = str.split(",")
        x[i] = XnY[0]
        y[i] = XnY[1]

plt.plot(x, y, linestyle="dashed", marker='o', color="red")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Chebyshev Polynomial Plot")
plt.savefig("chebyshev.png")