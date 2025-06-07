import numpy as np
import matplotlib.pyplot as plt

years = [2006 + x for x in range(16)]
weights = [80, 89, 43, 70, 59, 67, 89, 78, 78, 79, 76, 99, 88, 77, 78, 89 ]

plt.plot(years, weights, c="g", lw=3, linestyle="--")
plt.show()