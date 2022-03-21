import matplotlib.pyplot as plt
from prochazka import nahodna

fig,ax = plt.subplots(figsize = (12,7))

ax.scatter(nahodna.kroky_x,nahodna.kroky_y,s = 10, c=list(range(len(nahodna.kroky_y))), cmap="viridis")
ax.plot(nahodna.kroky_x,nahodna.kroky_y, ls ="--", c="k")
ax.scatter(nahodna.kroky_x[0],nahodna.kroky_y[0], s=50, c="red",label = "Start",edgecolors="k")
ax.scatter(nahodna.kroky_x[-1],nahodna.kroky_y[-1], s=50, c="black", label = "End",edgecolors="k")


ax.set_title("Nahodna prochazka",fontsize = 50)
ax.legend()
plt.show()