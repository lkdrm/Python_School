"""
class Zoo:
    def __init__(self):
        self.klece_v_zoo = []

    def pridej_klec_do_zoo(self,klec):
        self.klece_v_zoo.append(klec)

    def zvire_podle_barvy(self,barva):
        neexistuje = True
        for klec in self.klece_v_zoo:
            for zvire in klec.zvirata:
                if zvire.barva == barva:
                    print(zvire)
        if neexistuje:
            print("Neni takove zvire.")
"""

import matplotlib.pyplot as plt
import numpy as np


druhe_mocniny = [1,4,9,16,25]
treti_mocniny = [1,8,27,64,125]
cisla = np.arange(1,6)
#figure, axes = plt.subplots()

fig, ax = plt.subplots(figsize =(15,8))

ax.plot(cisla, druhe_mocniny, linewidth=5, color = "orange", linestyle = "dashed", label = "Druha mocnina")
ax.plot(cisla, treti_mocniny, lw = 6,      c = "b",          ls = ":",             label = "Treti mocnina")
ax.set_title("Graf druhych mocnin",fontsize = 25,)

ax.set_ylabel("Vysledek",fontsize = 15)
ax.set_xlabel("Cislo",fontsize = 15)
ax.legend(loc="upper right")

ax.tick_params(axis="both",which="major", labelsize=15)

plt.show()
