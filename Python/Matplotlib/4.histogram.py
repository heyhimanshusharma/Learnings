import numpy as np
import matplotlib.pyplot as plt

ages = np.random.normal(20, 1.5, 1000)

plt.hist(ages, bins=25)
plt.show()
plt.hist(ages, bins=25, cumulative=True)
plt.show()