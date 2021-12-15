year = int(input("How old are you?"))

drink = input("What do you prefer?")

wallet = 10

if year >= 18:
    print("Awesome , welcome")
    print("We glad to see you")
    if drink == "beer":
        print("We have several beers")
        print("Kozel,Radegast or Plzen")
        print("Which beer do you prefer?")
        pivo = input("Which beer do you want?")
        if pivo == "Kozel":
            wallet = wallet - 1
        elif pivo == "Radegast":
            wallet = wallet - 6
        elif pivo == "Plzen":
            wallet = wallet - 8
    else:
        print("Do you want something else? We have rum & wine")
elif year >= 15:
    print("Come inside we will give you a limonad!")
elif year >= 10:
    print("Come inside we have for you a djus")
else :
    print("Sorry , we don`t have for you to drink")

if year >= 20 and year <= 25:
    print("We have for you special drinks")

if year >= 60 or year <= 10:
    print("We have here something for seniors or kids")

print("End of program")