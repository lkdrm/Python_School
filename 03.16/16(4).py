import numpy as np
import matplotlib.pyplot as plt


druhe_mocniny = [1,4,9,16,25]

print(plt.style.available)
plt.style.use("dark_background")

#figure, axes = plt.subplots()

fig, ax = plt.subplots(druhe_mocniny)

ax.plot(druhe_mocniny)

plt.show()