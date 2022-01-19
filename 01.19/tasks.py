#1 Task:
"""
Napište program na počítání deště ve městech
Uživatel postupně zadává jméno města a déšť v milimetrech (nějaké
město se může zadat vícekrát). Pro ukončení zadá prázdný řádek.
Program pak vytiskne, kolik v každém městě napršelo.
Příklad (každý řádek je jedno zadání od uživatele):
Brno
10
Bratislava
15
Brno
20
(enter, tj. prázdný řádek)

Výsledek bude:
Brno: 30
Bratislava: 15
(nápověda: použijte slovník)

"""

def show_rain():
    my_list = {}
    while True:
        key = input("Enter a city:")
        if key == " ":
            break
        value_rain = input("Enter a rain milimetr:")
        my_list.setdefault(key,value_rain)
            
    return my_list   
        
def print_dict(pocasi):
    for key,value in pocasi.items():
        print(key,":", value )

print_dict(show_rain())
"""
Do when i write same city but another value 

count value and return 

Example:

I have Brno 30 and than 
i write Brno 10

print ( Brno 40)

"""