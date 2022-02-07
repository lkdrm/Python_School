"""
Cvičení na další část hodiny:
1.) Napište funkci, která vrátí seznam s třetími mocninami všech čísel 
v zadaném rozsahu.

2.) Vytvořte funkci, která vezme seznam čísel (list of ints) a 
vytvoří z nich řetězce.
2b.) Vytvoří řetězce jen z těch čísel, co jsou menší než 15.

3.) Sečtěte všechna čísla od 15 do 35 (můžete použít funcki sum).

4.) Napište funkci, která vezme čísla v zadaném rozsahu a 
vrátí řetězec, kde jsou daná čísla oddělená čárkami.

5.) Napište funkci, kter vezme řetězec, kde jsou čísla a 
shluky písmenek oddělená mezerami. Funkce vrátí součet čísel 
a písmenka ignoruje.
příklad: "10 abc 20 de44 30 55fg 40" -> 100

6.) Otočte slovník:
Vytvořte funkci, která vezme slovník a vytvoří nový slovník,
kde klíče jsou to, co bylo minule hodnoty a naopak

7.) Vytvočte funkci, která narovná seznam - tj. ze seznamu 
dvě úrovně hlubokého vytvoří seznam jednoúrovňový.
[[1,2], [3,4]] => [1, 2, 3, 4]
Asi budete potřebovat vnořený cyklus - v list comprehensions
lze vnořovat také, jen jsem vám to neukazoval. Zkuste to vymyslet.
"""

# 1 task:
# Napište funkci, která vrátí seznam s třetími mocninami všech čísel 
# v zadaném seznamu.
my_list = [1,2,3,4,5]

new_list_by_3 = [
    number ** 3
    for number in my_list
]

print(f"The new list : {new_list_by_3}")

# 2 task:
# Vytvořte funkci, která vezme seznam čísel (list of ints) a 
# vytvoří z nich řetězce.
# 2b.) Vytvoří řetězce jen z těch čísel, co jsou menší než 15.
