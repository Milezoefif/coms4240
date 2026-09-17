import matplotlib.pyplot as plt
import numpy as np

with open("data.txt", "r") as data_file:
    str = data_file.readline()

# Remove hanging delimiter
str = str[:-1]

exp = [float(val) for val in str.split(",")]

x = np.arange(0, 1.02, 0.02);

plt.plot(x, exp)
plt.xlabel("x")
plt.ylabel("exp(x)")
plt.savefig("exponent-data")
