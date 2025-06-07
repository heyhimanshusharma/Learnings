import numpy as np
import matplotlib.pyplot as plt

langs = ["Python", "C++", "Java", "C#", "Go"]
votes = [50, 24, 14, 6, 17]
explodes = [0.3, 0, 0, 0, 0]

plt.pie(votes, labels=langs, explode=explodes, autopct="%.2f%%", pctdistance=0.8, startangle=90)
plt.show()