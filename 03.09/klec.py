class Papousek:
    # staticka promena 
    # Class variable
    pocet_papousku = 0

    def __init__(self, name:str, color:str):
        self.name = name
        self.color = color
        self.__class__.pocet_papousku += 1

    def __str__(self):
        return f"Papousek ma jmeno {self.name} a ma barvu {self.color}"

class Klec():
    velikost = 3

    def __init__(self):
        self.papousci = []

    def pridej_papouska(self,papousek):
        if (len(self.papousci)) < self.__class__.velikost:
            self.papousci.append(papousek)
            print(f"Pridan papouse {papousek}")
        else:
            print("Papouska nelze pridat,je plno")

    def __str__(self):
        return f"Jsem klec a jsou ve me {len(self.papousci)} papousci"

class Velka_Klec(Klec):
    velikost = 5

    def __str__(self):
        return f"Jsem klec a jsou ve me {len(self.papousci)} papousci"   

prvni_papousek = Papousek("Boris","Zeleny")
druhy_papousek = Papousek("Richard","Zluty")
treti_papousek = Papousek("Karel","Cerveny")
ctvrti_papousek = Papousek("Amber","Black")

moje_klec = Klec()
moje_klec.pridej_papouska(prvni_papousek)
moje_klec.pridej_papouska(druhy_papousek)
moje_klec.pridej_papouska(treti_papousek)
moje_klec.pridej_papouska(ctvrti_papousek)

moje_big_klec = Velka_Klec()

moje_big_klec.pridej_papouska(prvni_papousek)
moje_big_klec.pridej_papouska(druhy_papousek)
moje_big_klec.pridej_papouska(treti_papousek)
moje_big_klec.pridej_papouska(ctvrti_papousek)

print(moje_klec)
print(moje_big_klec)

