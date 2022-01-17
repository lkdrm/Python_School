
menu_of_food = {
    "polevky":["porkova","borsh","drstova"],
    "hlavni jidlo":"Svickova",
    "desert":"zmrlina",
    "piti":["pivo","sladla voda",["voda","caj","kava"]],
    "vody":["sprite","cola","cofola"]
}

#print(menu_of_food["polevky"][1])
#print(menu_of_food["piti"][2][2])

menu_of_food["polevky"].append("s zely")

print(menu_of_food)

def see_keys (menu):
    for key in menu.keys():
        print("Nasi menu :",key)

def see_value(menu):
    for value in menu.values():
        if isinstance(value,list):
            for i in value:
                print("Nasi jidla:",i)
                if isinstance(i,list):
                    for b in i:
                        print("Nasi jidla:",b)

        print("Nasi jidla :", value)

key = see_keys(menu_of_food)
valu = see_value(menu_of_food)



