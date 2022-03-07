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

    @staticmethod
    def vypis_pocet_papousku_staticka_metoda():
        return f"Uz bylo vytvoreno {Papousek.pocet_papousku} papousku."

    @classmethod
    def vypis_pocet_papousku(cls):
        return f"Uz bylo vytvoreno {cls.pocet_papousku} papousku." # better version

#Statika

prvni_papousek = Papousek("Boris","Zeleny")
#print(prvni_papousek.name)

druhy_papousek = Papousek("Richard","Zluty")

treti_papousek = Papousek("Karel","Cerveny")

#print(Papousek.pocet_papousku)
#print(prvni_papousek.vypis_pocet_papousku())
print(Papousek.vypis_pocet_papousku_staticka_metoda())
print(Papousek.vypis_pocet_papousku())