import numpy as np
import matplotlib.pyplot as plt

x = ["C++", "C#", "Fortran", "C", "Python", "Java", "JavScript"]
y = [20, 50, 40, 70, 27, 40, 47]

plt.bar(x, y, color="r", align="edge", width=0.5, edgecolor="green")
plt.show()

# This makes sense for categorical data, not to be confused with histogram.
# It is a statistical plot, that shows the frequency of values on the x-axis.