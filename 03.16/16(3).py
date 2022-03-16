import numpy as np
import matplotlib.pyplot as plt

druhe_mocniny = [1,4,9,16,25]
treti_mocniny = [1,8,27,64,125]

print(plt.style.available)
plt.style.use("dark_background")

#figure, axes = plt.subplots()

fig, (ax1,ax2) = plt.subplots(nrows=1,ncols=2)

print(ax1)
print(ax2)

ax1.plot(druhe_mocniny)
ax1.set_title("Graf druhych mocnin")

ax2.plot(treti_mocniny)
ax2.set_title("Graf tretich mocnin")

plt.show()
#######################################################################
