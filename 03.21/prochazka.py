from random import choice,seed 

class NahodnaProchazka:
    def __init__(self,pocet_bodu = 5000):
        self.pocet_kroku = pocet_bodu
        self.kroky = []
        self.kroky_x = []
        self.kroky_y = []

    def vytvor(self):
        x = 0
        y = 0
        smer = [-1,1]
        rychlost = [0,1,2,3]
        #self.kroky.append((x,y))
        self.kroky_x.append(x)
        self.kroky_y.append(y)
        seed(53)
        for _ in range(self.pocet_kroku):
            smer_x = choice(smer)
            smer_y = choice(smer)
            rychlost_x = choice(rychlost)
            rychlost_y = choice(rychlost)
            x += smer_x * rychlost_x
            y += smer_y * rychlost_y
            #self.kroky.append((x,y))
            self.kroky_x.append(x)
            self.kroky_y.append(y)

nahodna = NahodnaProchazka(50)

nahodna.vytvor()

#print(nahodna.kroky_x)
#print(nahodna.kroky_y)
