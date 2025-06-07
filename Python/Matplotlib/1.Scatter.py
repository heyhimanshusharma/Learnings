import numpy as np
import matplotlib.pyplot as plt

X_data = np.random.random(500) * 100
Y_data = np.random.random(500) * 100

plt.scatter(X_data, Y_data, c="#00f", s=110, marker="*", alpha=0.5)
plt.show()
