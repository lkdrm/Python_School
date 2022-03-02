class Papousek:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name}, have a {self.color} color."

ara = Papousek("Pepik","red")
jumbo = Papousek("Honzik","green")
boris = Papousek("Boris","white")
richard = Papousek("Risa","yellow")

class Klec:
    def __init__(self):
        self.papousci = []

    def pridej_papouska(self,papousek):
        self.papousci.append(papousek)

    def __str__(self):
        if len(self.papousci) == 0:
            return "Jsem prazdna klec."
        obsah = " "
        for papousek in self.papousci:
           obsah += str(papousek) + ",\n"
        obsah = obsah[:-2]
        return f"Jsem klec na papousky a uvnitr je {obsah}."


klec_1 = Klec() 

#klec_1.papousci.append(boris)
klec_1.pridej_papouska(boris)
#klec_1.papousci.append(richard)
klec_1.pridej_papouska(richard)

print(klec_1)