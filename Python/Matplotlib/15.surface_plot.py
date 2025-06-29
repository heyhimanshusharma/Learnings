import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

ax = plt.axes(projection="3d")

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)

X, Y = np.meshgrid(x, y)

Z = np.sin(X) * np.cos(Y)

ax.plot_surface(X, Y, Z, cmap="Spectral")
plt.savefig("Spectrum.png")
plt.show()